# -*- coding: utf-8 -*-

import json
from string import lower
from cent.core import Client
from instant.utils import format_event_class
from instant.conf import SITE_NAME, CENTRIFUGO_HOST, CENTRIFUGO_PORT, SECRET_KEY, SITE_SLUG, PUBLIC_CHANNEL, BROADCAST_WITH
if BROADCAST_WITH == "go":
    import os, instant
    pth = os.path.dirname(instant.__file__)


def _get_channel(channel, target):
    if channel is None:
        if target is not None:
            if target == "superuser":
                channel = "$"+SITE_SLUG+'_admin'
            elif target == "staff":
                channel = "$"+SITE_SLUG+'_staff'
            elif target == "users":
                channel = "$"+SITE_SLUG+'_users'
            else:
                return False, None
        else:
            channel = PUBLIC_CHANNEL
    return channel

def broadcast_py(message, event_class="default", data={}, channel=None, site=SITE_NAME, message_label=None, target=None):
    cent_url = CENTRIFUGO_HOST+":"+str(CENTRIFUGO_PORT)
    client = Client(cent_url, SECRET_KEY, timeout=1)
    channel = _get_channel(channel, target)
    if message_label is None:
        message_label = format_event_class(obj=None, event_class=event_class)
    payload = {"message": message, "channel":channel, 'message_label':message_label, 'event_class':event_class, "data":data , "site":site}
    client.publish(channel, payload)
    if lower(event_class) == "debug":
        print "[DEBUG] "+str(json.dumps(payload))
    return True, channel

def broadcast_go(message, event_class="default", data={}, channel=None, site=SITE_NAME, message_label=None, target=None):
    channel = _get_channel(channel, target)
    channel = channel.replace("$","-_-")
    conn='-host="'+CENTRIFUGO_HOST+'" -port="'+str(CENTRIFUGO_PORT)+'" -key="'+SECRET_KEY+'"'
    params = conn+' -channel="'+channel+'" -event_class="'+event_class+'" -message="'+message+'" -data=\''+json.dumps(data)+"'"
    gocmd=pth+'/go/cent_broadcast '+params
    os.system(gocmd)
    return

if BROADCAST_WITH == "go":
    broadcast = broadcast_go
else:
    broadcast = broadcast_py