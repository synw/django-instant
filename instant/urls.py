# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.conf.urls import url
from django.views.generic import RedirectView
from instant.views import BroadcastView, StaffChannelView


urlpatterns = [
    url(r'^redirect-home/$', RedirectView.as_view(url=reverse_lazy('instant-broadcast')), name='instant-message-broadcasted'),
    url(r'^staff/$', StaffChannelView.as_view(), name="instant-staff-channel"),
    url(r'^', BroadcastView.as_view(), name="instant-broadcast")
]
