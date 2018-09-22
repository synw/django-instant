# -*- coding: utf-8 -*-
import json
from django.http import JsonResponse
from django.http.response import Http404
from django.views.generic.base import TemplateView
from django.views.decorators.csrf import csrf_exempt
from vv.views import PostFormView
from .producers import publish
from .utils import signed_response
from .apps import CHANNELS_NAMES


@csrf_exempt
def instant_auth(request):
    if not request.is_ajax() or not request.method == "POST":
        raise Http404
    chans = CHANNELS_NAMES
    data = json.loads(request.body.decode("utf-8"))
    channels = data["channels"]
    client = data['client']
    response = {}
    for channel in channels:
        signature = None
        if channel in chans["users"]:
            if request.user.is_authenticated:
                signature = signed_response(channel, client)
        if channel in chans["staff"]:
            if request.user.is_staff:
                signature = signed_response(channel, client)
        if channel in chans["superuser"]:
            if request.user.is_superuser:
                signature = signed_response(channel, client)
        # response
        if signature is not None:
            response[channel] = signature
        else:
            response[channel] = {"status": "403"}
    return JsonResponse(response)


class FrontendView(TemplateView):
    template_name = 'instant/frontend/index.html'
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404
        return super(FrontendView, self).dispatch(request, *args, **kwargs)


class PostMsgView(PostFormView):
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            raise Http404
        return super(PostMsgView, self).dispatch(request, *args, **kwargs)

    def action(self, request, clean_data):
        try:
            msg = clean_data["msg"]
            chan = clean_data["channel"]
            event_class = clean_data["msg_class"]
            data = clean_data["msg_data"]
            if data == "":
                data = {}
            else:
                data = json.loads(data)
            err = publish(msg, chan, event_class=event_class, data=data)
        except:
            err = "Error processing the message data"
        return None, err
