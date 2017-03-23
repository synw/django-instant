# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from vv.conf import VV_APPS


class IndexView(TemplateView):
    template_name = "vv/index.html"
