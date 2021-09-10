from typing import Any, Dict, Union

from cent import Client

from .conf import SITE_NAME, CENTRIFUGO_HOST, CENTRIFUGO_PORT, CENTRIFUGO_API_KEY


def publish(
    channel: str,
    *args,
    event_class: Union[str, None] = None,
    data: Union[Dict[Any, Any], None] = None,
    bucket: str = None,
    site: str = SITE_NAME
) -> None:
    """
    Publish a message to a websockets channel
    """
    message = None
    if len(args) == 1:
        message = args[0]
    if message is None and data is None:
        raise ValueError("Provide either a message or data argument")
    cent_url = CENTRIFUGO_HOST
    if CENTRIFUGO_PORT is not None:
        cent_url += ":" + str(CENTRIFUGO_PORT)
    client = Client(cent_url, api_key=CENTRIFUGO_API_KEY, timeout=1)
    payload: Dict[Any, Any] = {"channel": channel, "site": site}
    if message is not None:
        payload["message"] = message
    if data is not None:
        payload["data"] = data
    if event_class is not None:
        payload["event_class"] = event_class
    if bucket is not None:
        payload["bucket"] = bucket
    client.publish(channel, payload)
