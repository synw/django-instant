# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http.response import Http404
from django.views.generic import FormView
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages
from instant import broadcast
from instant.forms import BroadcastForm


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
        broadcast(message=msg, event_class=event_class, channel=channel)
        messages.info(self.request, _(u"Message broadcasted to the public channel"))
        return super(BroadcastView, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('instant-message-broadcasted')


