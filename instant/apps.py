from __future__ import unicode_literals
import os
from django.apps import AppConfig
from django.utils._os import safe_join


HANDLERS = []


class InstantConfig(AppConfig):
    name = 'instant'

    def ready(self):
        global HANDLERS
        from django.conf import settings
        from instant.utils import _ensure_channel_is_private
        from instant.conf import PUBLIC_CHANNELS, USERS_CHANNELS, \
            STAFF_CHANNELS, SUPERUSER_CHANNELS
        # ensure that the private channels are really private
        private_chans = USERS_CHANNELS + STAFF_CHANNELS + SUPERUSER_CHANNELS
        for chan in private_chans:
            _ensure_channel_is_private(chan)
        all_chans = private_chans + PUBLIC_CHANNELS
        if settings.INSTANT_DEBUG is True:
            print("Django Instant registered channels:")
            print("- Public:", PUBLIC_CHANNELS)
            print("- Users:", USERS_CHANNELS)
            print("- Staff", STAFF_CHANNELS)
            print("- Superuser", SUPERUSER_CHANNELS)
        # check if the default handler exists
        if len(all_chans) > 0:
            try:
                d = "templates/instant/handlers"
                handlers_dir = safe_join(settings.BASE_DIR, d)
                # map default handlers
                handlers = os.listdir(handlers_dir)
                for handler in handlers:
                    HANDLERS.append(handler.replace(".js", ""))
                if settings.INSTANT_DEBUG is True:
                    print("Handlers:", HANDLERS)
            except FileNotFoundError as e:
                if settings.INSTANT_DEBUG is True:
                    print("No handlers found for custom channels")
            except Exception as e:
                raise(e)
