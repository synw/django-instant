# -*- coding: utf-8 -*-

from django import VERSION
if VERSION >= (2, 0):
    from django.urls import reverse_lazy
else:
    from django.core.urlresolvers import reverse_lazy
from django.conf.urls import url
from django.views.generic import RedirectView
from instant.views import FrontendView, StaffChannelView, PostMsgView


urlpatterns = [
    url(r'^redirect-home/$', RedirectView.as_view(url=reverse_lazy('instant-broadcast')),
        name='instant-message-broadcasted'),
    url(r'^staff/$', StaffChannelView.as_view(), name="instant-staff-channel"),
    url(r'^rest/$', PostMsgView.as_view(), name="instant-post-msg"),
    url(r'^', FrontendView.as_view(), name="instant-broadcast")
]
