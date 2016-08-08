# -*- coding: utf-8 -*-

from django.core.exceptions import ImproperlyConfigured
from django.conf import settings


try:
    SECRET_KEY = getattr(settings, 'CENTRIFUGO_SECRET_KEY')
except ImportError:
    raise ImproperlyConfigured(u"The Centrifugo secret key must be set in settings.py with CENTRIFUGO_SECRET_KEY")
CENTRIFUGO_HOST = getattr(settings, 'CENTRIFUGO_HOST', 'http://localhost')
CENTRIFUGO_PORT = getattr(settings, 'CENTRIFUGO_PORT', 8001)

REDIS_HOST = getattr(settings, 'MQUEUE_REDIS_HOST', 'localhost')
REDIS_PORT = getattr(settings, 'MQUEUE_REDIS_PORT', 6379)
REDIS_DB = getattr(settings, 'MQUEUE_REDIS_DB', 0)

SITE_SLUG =  getattr(settings, 'SITE_SLUG', 'site')
GLOBAL_STREAMS =  getattr(settings, 'INSTANT_GLOBAL_STREAMS', ())

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