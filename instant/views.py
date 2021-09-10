import json

from django.contrib import auth
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

from .token import connection_token, channel_token
from .models import Channel


@csrf_exempt
def private_channel_subscription(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    json_data = json.loads(request.body)
    # print("PRIVATE SUB for", request.user.username, json_data)
    user_chans = Channel.objects.for_user(request.user).values("name")  # type: ignore
    user_chans_names = []
    for chan in user_chans:
        user_chans_names.append(chan["name"])
    authorized_chans = []
    for channel in json_data["channels"]:
        # print("Checking auth for chan", channel, channel in user_chans_names)
        if channel in user_chans_names:
            chan = {
                "channel": channel,
                "token": channel_token(json_data["client"], channel),
            }
            authorized_chans.append(chan)
    # print({"channels": authorized_chans})
    return JsonResponse({"channels": authorized_chans})


def _get_response(request):
    channels = Channel.objects.for_user(request.user).values(  # type: ignore
        "name", "level"
    )
    return JsonResponse(
        {
            "csrf_token": get_token(request),
            "ws_token": connection_token(request.user),
            "channels": list(channels),
        }
    )


@csrf_exempt
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


@csrf_exempt
def get_connection_token(request):
    if not request.user.is_authenticated:
        return HttpResponseForbidden()
    return _get_response(request)
