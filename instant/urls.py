# -*- coding: utf-8 -*-
from django.urls import path
from .views import (
    login_and_get_tokens,
    logout,
    get_connection_token,
    private_channel_subscription,
)

urlpatterns = [
    path("login/", login_and_get_tokens, name="instant-login"),
    path("logout/", logout, name="instant-logout"),
    path("get_token/", get_connection_token, name="instant-get-token"),
    path("subscribe/", private_channel_subscription, name="instant-subscribe"),
]
