# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


try:
    SECRET_KEY = getattr(settings, 'CENTRIFUGO_SECRET_KEY')
except ImportError:
    raise ImproperlyConfigured(u"The Centrifugo secret key must be set in settings.py with CENTRIFUGO_SECRET_KEY")
CENTRIFUGO_HOST = getattr(settings, 'CENTRIFUGO_HOST', 'http://localhost')
CENTRIFUGO_PORT = getattr(settings, 'CENTRIFUGO_PORT', 8001)

SITE_SLUG =  getattr(settings, 'SITE_SLUG', 'site')
SITE_NAME =  getattr(settings, 'SITE_NAME', 'Site')

BROADCAST_WITH = getattr(settings, 'INSTANT_BROADCAST_WITH', "py")

ENABLE_USERS_CHANNEL = getattr(settings, 'INSTANT_ENABLE_USERS_CHANNEL', False)
ENABLE_STAFF_CHANNEL = getattr(settings, 'INSTANT_ENABLE_STAFF_CHANNEL', False)
ENABLE_SUPERUSER_CHANNEL = getattr(settings, 'INSTANT_ENABLE_SUPERUSER_CHANNEL', False)

public_channel = SITE_SLUG+'_public'
PUBLIC_CHANNEL =  getattr(settings, 'INSTANT_PUBLIC_CHANNEL', public_channel)
USERS_CHANNELS =  getattr(settings, 'INSTANT_USERS_CHANNELS', ["$"+SITE_SLUG+"_users"])
STAFF_CHANNELS =  getattr(settings, 'INSTANT_STAFF_CHANNELS', ["$"+SITE_SLUG+"_staff"])
SUPERUSER_CHANNELS =  getattr(settings, 'INSTANT_SUPERUSER_CHANNELS', ["$"+SITE_SLUG+"_admin"])

# ensure that the private channels will always be treated as private by Centrifugo
chans = []
for chan in USERS_CHANNELS:
    if not chan.startswith("$"):
        chan = u"$"+chan
    chans.append(chan)
USERS_CHANNELS = chans
schans = []
for chan in STAFF_CHANNELS:
    if not chan.startswith("$"):
        chan = u"$"+chan
    schans.append(chan)
STAFF_CHANNELS = schans
achans = []
for chan in SUPERUSER_CHANNELS:
    if not chan.startswith("$"):
        chan = u"$"+chan
    achans.append(chan)
SUPERUSER_CHANNELS = achans