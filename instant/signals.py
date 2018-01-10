# -*- coding: utf-8 -*-
import json
from django.conf import settings


def channel_delete(sender, instance, **kwargs):
    from .apps import set_channels
    chans = set_channels(settings)
    if settings.INSTANT_DEBUG is True:
        print("Database channel deleted:")
        print(json.dumps(chans, indent=2))


def channel_save(sender, instance, created, **kwargs):
    from .apps import set_channels
    chans = set_channels(settings)
    if settings.INSTANT_DEBUG is True:
        word = "updated"
        if created is True:
            word = "created"
        print("Database channel " + word + ":")
        print(json.dumps(chans, indent=2))
