# -*- coding: utf-8 -*-

from cent.core import Client
from mqueue.utils import format_event_class
from instant.conf import GLOBAL_STREAMS, CENTRIFUGO_HOST, CENTRIFUGO_PORT, SITE_SLUG, SECRET_KEY


def _get_public_channel():
    channel = SITE_SLUG+'_public'
    if 'public' in GLOBAL_STREAMS:
        channel = "public"
    return channel

def broadcast(message, event_class=None, channel=None):
    cent_url = CENTRIFUGO_HOST+":"+str(CENTRIFUGO_PORT)
    client = Client(cent_url, SECRET_KEY, timeout=1)
    if channel is None:
        channel = _get_public_channel()
    msg_label = format_event_class(obj=None, event_class=event_class)
    data = {"message": message, 'message_label':msg_label, 'event_class':event_class }
    client.publish(channel, data)
    return