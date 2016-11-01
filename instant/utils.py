# -*- coding: utf-8 -*-

from cent.core import generate_channel_sign
from instant.conf import PUBLIC_CHANNEL, SECRET_KEY


def signed_response(channel, client):
    signature = generate_channel_sign(SECRET_KEY, client, channel, info="")
    return {"sign": signature}


def _get_public_channel():
    return PUBLIC_CHANNEL
