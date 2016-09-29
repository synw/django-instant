# -*- coding: utf-8 -*-

import json
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from instant.producers import broadcast
from instant.forms import BroadcastForm
from instant.utils import signed_response
from instant.conf import USERS_CHANNELS, STAFF_CHANNELS, SUPERUSER_CHANNELS


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
            if request.user.is_staff:
                signature = signed_response(channel, client)
        if channel in SUPERUSER_CHANNELS:
            if request.user.is_superuser:
                signature = signed_response(channel, client)
        if signature is not None:
            response[channel] = signature
        else:
            response[channel] = {"status","403"}
    return JsonResponse(response)


class StaffChannelView(TemplateView):
    template_name = 'instant/channels/staff.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.is_ajax():
            raise Http404
        return super(StaffChannelView, self).dispatch(request, *args, **kwargs)


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
        default_channel = form.cleaned_data['default_channel']
        if channel or default_channel:
            if default_channel:
                broadcast(message=msg, event_class=event_class, channel=default_channel)
            if channel:
                broadcast(message=msg, event_class=event_class, channel=channel)
            messages.success(self.request, _(u"Message broadcasted to the channel "+channel))
        else:
            messages.warning(self.request, _(u"Please provide a valid channel"))
        return super(BroadcastView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('instant-message-broadcasted')