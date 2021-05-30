# -*- coding: utf-8 -*-
from django.apps import AppConfig


class InstantConfig(AppConfig):
    name = 'instant'

    def ready(self):
        pass
