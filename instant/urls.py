# -*- coding: utf-8 -*-
from django.conf.urls import url
from instant.views import FrontendView, PostMsgView

urlpatterns = [
    url(r'^post/$', PostMsgView.as_view(), name="instant-post-msg"),
    url(r'^', FrontendView.as_view(), name="instant-frontend")
]
