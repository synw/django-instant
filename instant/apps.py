from __future__ import unicode_literals
import os
from django.apps import AppConfig
from django.core.exceptions import ImproperlyConfigured


HANDLERS = []


class InstantConfig(AppConfig):
    name = 'instant'

    def ready(self):
        global HANDLERS
        from django.conf import settings
        from instant.utils import _ensure_channel_is_private
        from instant.conf import PUBLIC_CHANNELS, USERS_CHANNELS, STAFF_CHANNELS, SUPERUSER_CHANNELS
        # ensure that the private channels are really private
        private_chans = USERS_CHANNELS + STAFF_CHANNELS + SUPERUSER_CHANNELS
        for chan in private_chans:
            _ensure_channel_is_private(chan)
        all_chans = private_chans + PUBLIC_CHANNELS
        handlers_dir = settings.BASE_DIR + "/templates/instant/handlers"
        # check if the default handler exists
        if len(all_chans) > 0:
            msg = "Please create a /templates/instant/handlers/default.js file for your custom channels"
            if os.path.isdir(handlers_dir) is False:
                raise ImproperlyConfigured(msg)
            if os.path.exists(handlers_dir + "/default.js") is False:
                raise ImproperlyConfigured(msg)
        # map default handlers
        handlers = os.listdir(handlers_dir)
        for handler in handlers:
            HANDLERS.append(handler.replace(".js", ""))
