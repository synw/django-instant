# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.apps import AppConfig
from django.utils._os import safe_join


HANDLERS = []
CHANNELS = {}
CHANNELS_NAMES = {}


class InstantConfig(AppConfig):
    name = 'instant'

    def ready(self):
        global HANDLERS, CHANNELS, CHANNELS_NAMES
        from django.conf import settings
        from .utils import get_channels_for_roles
        CHANNELS, CHANNELS_NAMES = get_channels_for_roles()
        try:
            if settings.INSTANT_DEBUG is True:
                print("Django Instant registered channels:")
                print(json.dumps(CHANNELS, indent=2))
        except AttributeError:
            pass
        # check if the default handler exists
        try:
            d = "templates/instant/handlers"
            handlers_dir = safe_join(settings.BASE_DIR, d)
            # map default handlers
            handlers = os.listdir(handlers_dir)
            for handler in handlers:
                HANDLERS.append(handler.replace(".js", ""))
            try:
                if settings.INSTANT_DEBUG is True:
                    print("Handlers:", HANDLERS)
            except AttributeError:
                pass
        except FileNotFoundError as e:
            try:
                if settings.INSTANT_DEBUG is True:
                    print("No handlers found for custom channels")
            except AttributeError:
                pass
        except Exception as e:
            raise(e)
