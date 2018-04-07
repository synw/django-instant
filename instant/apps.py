# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.apps import AppConfig
from django.utils._os import safe_join

# -*- coding: utf-8 -*-
HANDLERS = []
CHANNELS = {}
CHANNELS_NAMES = {}


def set_channels(settings):
    from .utils import get_channels_for_roles
    global CHANNELS, CHANNELS_NAMES
    CHANNELS, CHANNELS_NAMES = get_channels_for_roles()
    try:
        if getattr(settings, "INSTANT_DEBUG", False) is True:
            print("Django Instant registered channels:")
            print(json.dumps(CHANNELS, indent=2))
    except Exception:
        pass
    return CHANNELS


def connect_signals():
    from django.db.models.signals import post_save, post_delete
    from .signals import channel_delete, channel_save
    from .models import Channel
    post_save.connect(channel_save, sender=Channel)
    post_delete.connect(channel_delete, sender=Channel)


class InstantConfig(AppConfig):
    name = 'instant'

    def ready(self):
        global HANDLERS, CHANNELS, CHANNELS_NAMES
        from django.conf import settings
        DEBUG = getattr(settings, "INSTANT_DEBUG", False)
        set_channels(settings)
        # check if the default handler exists
        try:
            d = "templates/instant/handlers"
            handlers_dir = safe_join(settings.BASE_DIR, d)
            # map default handlers
            handlers = os.listdir(handlers_dir)
            for handler in handlers:
                HANDLERS.append(handler.replace(".js", ""))
            try:
                if DEBUG is True:
                    print("Handlers:", HANDLERS)
            except Exception:
                pass
        except FileNotFoundError as e:
            try:
                if DEBUG is True:
                    print("No handlers found for custom channels")
            except Exception:
                pass
        except Exception as e:
            raise(e)
        # connect model signals
        connect_signals()
