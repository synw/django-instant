# -*- coding: utf-8 -*-

import time
from django import template
from django.conf import settings
from cent.core import generate_token, Client


DEBUG = False

try:
    SECRET_KEY = getattr(settings, 'CENTRIFUGO_SECRET_KEY')
except ImportError:
    raise ImproperlyConfigured(u"The Centrifugo secret key must be set in settings.py with CENTRIFUGO_SECRET_KEY")
SITE_SLUG =  getattr(settings, 'SITE_SLUG', 'site')
CENTRIFUGO_HOST = getattr(settings, 'CENTRIFUGO_HOST', 'http://localhost')
CENTRIFUGO_PORT = getattr(settings, 'CENTRIFUGO_PORT', 8001)

REDIS_HOST = getattr(settings, 'MQUEUE_REDIS_HOST', 'localhost')
REDIS_PORT = getattr(settings, 'MQUEUE_REDIS_PORT', 6379)
REDIS_DB = getattr(settings, 'MQUEUE_REDIS_DB', 0)

GLOBAL_STREAMS =  getattr(settings, 'INSTANT_GLOBAL_STREAMS', ())
APPS =  getattr(settings, 'INSTANT_APPS', [])

def _get_public_channel():
    channel = SITE_SLUG+'_public'
    if 'public' in GLOBAL_STREAMS:
        channel = "public"
    return channel

register = template.Library()

@register.simple_tag
def get_centrifugo_url():
    return CENTRIFUGO_HOST+":"+str(CENTRIFUGO_PORT)

@register.simple_tag
def get_timestamp():
    return str(int(time.time()))

@register.simple_tag
def mq_generate_token(user, timestamp, info=""):
    token = generate_token(SECRET_KEY, user, timestamp, info)
    if DEBUG is True:
        print "Generating token:"
        print "Key: "+SECRET_KEY
        print "User: "+user
        print "Timestamp: "+timestamp
        print "Generated token for user "+user+" at "+timestamp+": "+token
    return token

@register.simple_tag
def get_public_channel():
    return _get_public_channel()

@register.simple_tag
def get_apps():
    return APPS



