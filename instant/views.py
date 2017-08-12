# -*- coding: utf-8 -*-

import json
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.views.generic.base import View
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from instant.producers import publish
from instant.forms import BroadcastForm
from instant.utils import signed_response, _get_chans_from_conf
from instant.conf import USERS_CHANNELS, STAFF_CHANNELS, SUPERUSER_CHANNELS,\
    DEFAULT_SUPERUSER_CHANNEL, DEFAULT_STAFF_CHANNEL, USERS_CHANNELS


SUPERCHANS = _get_chans_from_conf(SUPERUSER_CHANNELS)
STAFFCHANS = _get_chans_from_conf(STAFF_CHANNELS)
USERSCHANS = _get_chans_from_conf(USERS_CHANNELS)


@csrf_exempt
def instant_auth(request):
    global SUPERCHANS
    global STAFFCHANS
    global USERSCHANS
    if not request.is_ajax() or not request.method == "POST":
        raise Http404
    data = json.loads(request.body.decode("utf-8"))
    channels = data["channels"]
    client = data['client']
    response = {}
    for channel in channels:
        signature = None
        # old systems: will be DEPRECATED
        if channel in USERS_CHANNELS:
            if request.user.is_authenticated():
                signature = signed_response(channel, client)
        if channel in STAFF_CHANNELS or channel == DEFAULT_STAFF_CHANNEL:
            if request.user.is_staff:
                signature = signed_response(channel, client)
        if channel == DEFAULT_SUPERUSER_CHANNEL:
            if request.user.is_superuser:
                signature = signed_response(channel, client)
        # new system
        if request.user.is_superuser:
            for chan in SUPERCHANS:
                if chan == channel:
                    signature = signed_response(channel, client)
        if request.user.is_staff:
            for chan in STAFFCHANS:
                if chan == channel:
                    signature = signed_response(channel, client)
        if request.user.is_authenticated:
            for chan in USERSCHANS:
                if chan == channel:
                    signature = signed_response(channel, client)
        # response
        if signature is not None:
            response[channel] = signature
        else:
            response[channel] = {"status": "403"}
    return JsonResponse(response)


class StaffChannelView(TemplateView):
    template_name = 'instant/channels/staff.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.is_ajax():
            raise Http404
        return super(StaffChannelView, self).dispatch(request, *args, **kwargs)


class FrontendView(FormView):
    form_class = BroadcastForm
    template_name = 'instant/frontend/index.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404
        return super(FrontendView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        print(form.cleaned_data)

        msg = form.cleaned_data['message']
        event_class = "default"
        if "event_class" in form.cleaned_data:
            event_class = form.cleaned_data['event_class']
        channel = form.cleaned_data['channel']
        default_channel = form.cleaned_data['default_channel']
        err = None
        if channel or default_channel:
            if default_channel:
                err = publish(message=msg, event_class=event_class,
                              channel=default_channel)
            if channel:
                err = publish(
                    message=msg, event_class=event_class, channel=channel)
            if err is not None:
                messages.warning(self.request, _(
                    u"Error publishing the message: " + err))
            else:
                messages.success(self.request, _(
                    u"Message published to the channel " + channel))
        else:
            messages.warning(self.request, _(
                u"Please provide a valid channel"))
        return super(FrontendView, self).form_valid(form)

    def get_success_url(self):
        return reverse('instant-message-broadcasted')


class PostMsgView(View):

    def post(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return JsonResponse({"ok": 0})
        data = json.loads(self.request.body.decode('utf-8'))
        msg = data["msg"]
        channel = data["channel"]
        event_class = "default"
        if "event_class" in data:
            event_class = data['event_class']
        err = publish(message=msg, event_class=event_class, channel=channel)
        if err is not None:
            errmsg = _(u"Error publishing the message: " + err)
            return JsonResponse({"ok": 0, "err": errmsg})
        return JsonResponse({"ok": 1})
