# -*- coding: utf-8 -*-

from cent.core import Client
from instant.conf import GLOBAL_STREAMS, CENTRIFUGO_HOST, CENTRIFUGO_PORT, SITE_SLUG, SECRET_KEY, EVENT_CLASSES, EVENT_ICONS_HTML, EVENT_EXTRA_HTML


def _get_public_channel():
    channel = SITE_SLUG+'_public'
    if 'public' in GLOBAL_STREAMS:
        channel = "public"
    return channel

def broadcast(message, event_class="default", channel=None):
    cent_url = CENTRIFUGO_HOST+":"+str(CENTRIFUGO_PORT)
    client = Client(cent_url, SECRET_KEY, timeout=1)
    if channel is None:
        channel = _get_public_channel()
    msg_label = format_event_class(obj=None, event_class=event_class)
    data = {"message": message, 'message_label':msg_label, 'event_class':event_class }
    client.publish(channel, data)
    return

def get_event_class_str(event_class):
    event_class_str = 'Default'
    if 'created' in event_class:
        event_class_str = 'Object created'
    if 'deleted' in event_class:
        event_class_str = 'Object deleted'
    if 'edited' in event_class:
        event_class_str = 'Object edited'
    return event_class_str

def format_event_class(obj=None, event_class=None):
    event_html = ''
    if event_class is None:
        event_class = obj.event_class
    else:
        event_class = event_class
    printed_class = get_event_class_str(event_class)
    icon = ''
    if event_class in EVENT_ICONS_HTML.keys():
        icon = EVENT_ICONS_HTML[event_class]+'&nbsp;'
        printed_class = event_class
    else:
        if 'created' in event_class:
            icon = EVENT_ICONS_HTML['Object created']+'&nbsp;'
        elif 'edited' in event_class:
            icon = EVENT_ICONS_HTML['Object edited']+'&nbsp;'
        elif 'deleted' in event_class:
            icon = EVENT_ICONS_HTML['Object deleted']+'&nbsp;'
        else:
            icon = EVENT_ICONS_HTML['Default']+'&nbsp;'
        if 'error' in event_class.lower():
            icon = EVENT_ICONS_HTML['Error']+'&nbsp;'
            printed_class = 'Error'
        elif 'debug' in event_class.lower():
            icon = EVENT_ICONS_HTML['Debug']+'&nbsp;'
            printed_class = 'Debug'
        elif 'warning' in event_class.lower():
            icon = EVENT_ICONS_HTML['Warning']+'&nbsp;'
            printed_class = 'Warning'
        elif 'info' in event_class.lower():
            icon = EVENT_ICONS_HTML['Info']+'&nbsp;'
            printed_class = 'Info'
        elif 'important' in event_class.lower():
            icon = EVENT_ICONS_HTML['Important']+'&nbsp;'
            printed_class = 'Important'
    if event_class in EVENT_CLASSES.keys():
        event_html += '<span class="'+EVENT_CLASSES[printed_class]+'">'+icon+event_class+'</span>'
    else:
        event_html += '<span class="'+EVENT_CLASSES[printed_class]+'">'+icon+event_class+'</span>'
    if event_class in EVENT_EXTRA_HTML.keys():
        event_html += EVENT_EXTRA_HTML[event_class]
    return event_html