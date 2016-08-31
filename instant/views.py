# -*- coding: utf-8 -*-

import json
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.views.generic import FormView
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from instant import broadcast
from instant.forms import BroadcastForm
from django.views.decorators.csrf import csrf_exempt
from cent.core import generate_channel_sign
from instant.conf import SECRET_KEY, USERS_CHANNELS, STAFF_CHANNELS, SUPERUSER_CHANNELS


def signed_response(channel, client):
    signature = generate_channel_sign(SECRET_KEY, client, channel, info="")
    return {"sign": signature}

@csrf_exempt
def instant_auth(request):
    if not request.is_ajax() or not request.method == "POST":
        raise Http404
    data = json.loads(request.body)
    channels = data["channels"]
    client = data['client']
    response = {}
    for channel in channels:
        signature = None
        if channel in USERS_CHANNELS:
            if request.user.is_authenticated():
                signature = signed_response(channel, client)
        if channel in STAFF_CHANNELS:
            if request.user.is_staff():
                signature = signed_response(channel, client)
        if channel in SUPERUSER_CHANNELS:
            if request.user.is_superuser:
                signature = signed_response(channel, client)
        if signature is not None:
            response[channel] = signature
        else:
            response[channel] = {"status","403"}  
    return JsonResponse(response)


class BroadcastView(FormView):
    form_class = BroadcastForm
    template_name = 'instant/broadcast.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404
        return super(BroadcastView, self).dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        msg = form.cleaned_data['message']
        event_class = form.cleaned_data['event_class']
        channel = form.cleaned_data['channel']
        broadcast(message=msg, event_class=event_class, channel=channel)
        messages.info(self.request, _(u"Message broadcasted to the public channel"))
        return super(BroadcastView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('instant-message-broadcasted')


