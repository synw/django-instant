# -*- coding: utf-8 -*-
from django.apps import AppConfig


class InstantConfig(AppConfig):
    name = "instant"
    default_auto_field = "django.db.models.BigAutoField"

    def ready(self):
        pass
