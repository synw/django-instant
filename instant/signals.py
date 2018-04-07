# -*- coding: utf-8 -*-
import json
from django.conf import settings


DEBUG = getattr(settings, "INSTANT_DEBUG", False)


def channel_delete(sender, instance, **kwargs):
    global DEBUG
    from .apps import set_channels
    chans = set_channels(settings)
    if DEBUG is True:
        print("Database channel deleted:")
        print(json.dumps(chans, indent=2))


def channel_save(sender, instance, created, **kwargs):
    global DEBUG
    from .apps import set_channels
    chans = set_channels(settings)
    if DEBUG is True:
        word = "updated"
        if created is True:
            word = "created"
        print("Database channel " + word + ":")
        print(json.dumps(chans, indent=2))
