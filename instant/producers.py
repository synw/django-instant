# -*- coding: utf-8 -*-

import json
from cent import Client, CentException
from .conf import SITE_NAME, CENTRIFUGO_HOST, CENTRIFUGO_PORT, CENTRIFUGO_API_KEY


def publish(
    channel, message, event_class="default", data={}, bucket=None, site=SITE_NAME
):

    cent_url = CENTRIFUGO_HOST
    if CENTRIFUGO_PORT is not None:
        cent_url += ":" + str(CENTRIFUGO_PORT)
    client = Client(cent_url, api_key=CENTRIFUGO_API_KEY, timeout=1)
    payload = {
        "message": message,
        "channel": channel,
        "event_class": event_class,
        "bucket": bucket,
        "data": data,
        "site": site,
    }
    err = None
    try:
        print(f"Publishing to {cent_url} {payload}")
        client.publish(channel, payload)
    except CentException as e:
        err = str(e)
    except Exception as e:
        raise e
    if event_class.lower() == "debug":
        print("[DEBUG] ", str(json.dumps(payload)))
    return err
