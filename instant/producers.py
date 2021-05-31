# -*- coding: utf-8 -*-

from cent import Client, CentException
from .conf import SITE_NAME, CENTRIFUGO_HOST, CENTRIFUGO_PORT, CENTRIFUGO_API_KEY


def publish(channel, *args, event_class=None, data=None, bucket=None, site=SITE_NAME):
    message = None
    if len(args) == 1:
        message = args[0]
    if message is None and data is None:
        raise ValueError("Provide either a message or data argument")
    cent_url = CENTRIFUGO_HOST
    if CENTRIFUGO_PORT is not None:
        cent_url += ":" + str(CENTRIFUGO_PORT)
    client = Client(cent_url, api_key=CENTRIFUGO_API_KEY, timeout=1)
    payload = {"channel": channel, "site": site}
    if message is not None:
        payload["message"] = message
    if data is not None:
        payload["data"] = data
    if event_class is not None:
        payload["event_class"] = event_class
    if bucket is not None:
        payload["bucket"] = bucket
    err = None
    try:
        print(f"Publishing to {cent_url} {payload}")
        client.publish(channel, payload)
    except CentException as e:
        err = str(e)
    except Exception as e:
        raise e
    return err
