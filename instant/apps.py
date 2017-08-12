from __future__ import unicode_literals
from django.apps import AppConfig


class InstantConfig(AppConfig):
    name = 'instant'

    def ready(self):
        from instant.utils import _ensure_channel_is_private
        from instant.conf import USERS_CHANNELS, STAFF_CHANNELS, SUPERUSER_CHANNELS
        # ensure that the private channels are really private
        private_chans = USERS_CHANNELS + STAFF_CHANNELS + SUPERUSER_CHANNELS
        for chan in private_chans:
            _ensure_channel_is_private(chan)
