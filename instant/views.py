import json

from django.contrib import auth
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

from .token import connection_token, channel_token
from .models import Channel

def user_channels(user):
    user_chans = Channel.objects.for_user(user)
    authorized_chans = []
    for channel in user_chans:
        # print("Checking auth for chan", channel, channel in user_chans_names)
        chan = {
            "name": channel.name,
            "level": channel.level,
            "token": channel_token(channel.name, user),
        }
        authorized_chans.append(chan)
    return authorized_chans


@csrf_exempt  # type: ignore
def channels_subscription(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    json_data = json.loads(request.body)
    # print("PRIVATE SUB for", request.user.username, json_data)
    user_chans = Channel.objects.for_user(request.user).values("name")  # type: ignore
    user_chans_names = []
    for chan in user_chans:
        user_chans_names.append(chan["name"])
    authorized_chans = user_channels(request.user)
    # print({"channels": authorized_chans})
    return JsonResponse({"channels": authorized_chans})


def _get_response(request):
    channels = user_channels(request.user)
    return JsonResponse(
        {
            "csrf_token": get_token(request),
            "ws_token": connection_token(request.user),
            "channels": channels,
        }
    )


@csrf_exempt  # type: ignore
def login_and_get_tokens(request):
    # print("Login view", request.method)
    if request.user.is_authenticated:
        return _get_response(request)
    if request.method == "POST":
        # print("POST", request.body)
        json_data = json.loads(request.body)
        username = json_data["username"]
        password = json_data["password"]
        # print("Authenticate", username, password)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return _get_response(request)
    return HttpResponseForbidden()


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return JsonResponse({"response": "ok"})
    return HttpResponseForbidden()


@csrf_exempt  # type: ignore
def get_connection_token(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    return _get_response(request)
