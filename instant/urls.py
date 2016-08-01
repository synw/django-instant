# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse_lazy
from django.conf.urls import patterns, url
from django.views.generic import RedirectView, TemplateView
from instant.views import BroadcastView


urlpatterns = patterns('',
    url(r'^redirect-home/$', RedirectView.as_view(url=reverse_lazy('instant-broadcast')), name='instant-message-broadcasted'),
    url(r'^', BroadcastView.as_view(), name="instant-broadcast"),
)
