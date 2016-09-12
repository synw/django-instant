# -*- coding: utf-8 -*-

from string import lower
from cent.core import Client
from instant.utils import format_event_class
from instant.conf import SITE_NAME, CENTRIFUGO_HOST, CENTRIFUGO_PORT, SECRET_KEY, SITE_SLUG


def broadcast(message, event_class="default", data={}, channel=None, site=SITE_NAME, message_label=None, target=None):
    cent_url = CENTRIFUGO_HOST+":"+str(CENTRIFUGO_PORT)
    client = Client(cent_url, SECRET_KEY, timeout=1)
    if channel is None:
        if target is not None:
            if target == "superuser":
                channel = "$"+SITE_SLUG+'_admin'
            if target == "staff":
                channel = "$"+SITE_SLUG+'_staff'
            if target == "users":
                channel = "$"+SITE_SLUG+'_users'
            else:
                return False, None
        else:
            _get_public_channel()
    if message_label is None:
        message_label = format_event_class(obj=None, event_class=event_class)
    payload = {"message": message, "channel":channel, 'message_label':message_label, 'event_class':event_class, "data":data , "site":site}
    client.publish(channel, payload)
    if lower(event_class) == "debug":
        print "[DEBUG] "+str(json.dumps(payload))
    return True, channel