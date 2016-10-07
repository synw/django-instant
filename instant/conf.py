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
USERS_CHANNELS =  getattr(settings, 'INSTANT_USERS_CHANNELS', [])
STAFF_CHANNELS =  getattr(settings, 'INSTANT_STAFF_CHANNELS', [])
SUPERUSER_CHANNELS =  getattr(settings, 'INSTANT_SUPERUSER_CHANNELS', [])
# add default channels
if ENABLE_USERS_CHANNEL is True:
    USERS_CHANNELS.append("$"+SITE_SLUG+"_users")
if ENABLE_STAFF_CHANNEL is True:
    STAFF_CHANNELS.append("$"+SITE_SLUG+"_staff")
if ENABLE_SUPERUSER_CHANNEL is True:
    SUPERUSER_CHANNELS.append("$"+SITE_SLUG+"_admin")

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

# ===================== Events formats ===================================
EVENT_CLASSES = {
                 #~ 'Event class label' : 'css class to apply',
                'Default' : 'mq-label mq-default',
                'Important' : 'mq-label mq-important',
                'Ok' : 'mq-label mq-ok',
                'Info' : 'mq-label mq-info',
                'Debug' : 'mq-label mq-debug',
                'Warning' : 'mq-label mq-warning',
                'Error' : 'mq-label mq-error',
                'Object created' : 'mq-label mq-created',
                'Object edited' : 'mq-label mq-edited',
                'Object deleted' : 'mq-label mq-deleted',
                }

EVENT_CLASSES=getattr(settings, 'MQUEUE_EVENT_CLASSES', EVENT_CLASSES)

EVENT_ICONS_HTML = {
                 #~ 'Event class label' : 'icon css class',
                'Default' : '<i class="fa fa-flash"></i>',
                'Important' : '<i class="fa fa-exclamation"></i>',
                'Ok' : '<i class="fa fa-thumbs-up"></i>',
                'Info' : '<i class="fa fa-info-circle"></i>',
                'Debug' : '<i class="fa fa-cog"></i>',
                'Warning' : '<i class="fa fa-exclamation"></i>',
                'Error' : '<i class="fa fa-exclamation-triangle"></i>',
                'Object edited' : '<i class="fa fa-pencil"></i>',
                'Object created' : '<i class="fa fa-plus"></i>',
                'Object deleted' : '<i class="fa fa-remove"></i>',
                }

EVENT_ICONS_HTML=getattr(settings, 'MQUEUE_EVENT_ICONS_HTML', EVENT_ICONS_HTML)

EVENT_EXTRA_HTML=getattr(settings, 'MQUEUE_EVENT_EXTRA_HTML', {})