# -*- coding: utf-8 -*-

from cent.core import generate_channel_sign
from instant.conf import PUBLIC_CHANNEL, SECRET_KEY


def signed_response(channel, client):
    signature = generate_channel_sign(SECRET_KEY, client, channel, info="")
    return {"sign": signature}


def _get_public_channel():
    return PUBLIC_CHANNEL


def _get_chans_from_conf(chanconf, path=None):
    if path is not None:
        lastchar = path[-1:]
        if lastchar == "/":
            path = path[:-1]
    chans = []
    for chantup in chanconf:
        chan = chantup[0]
        chanpaths = []
        if len(chantup) == 1 or path is None:
            chans.append(chan)
        else:
            chanpaths = chantup[1]
            for chanpath in chanpaths:
                if chanpath == path:
                    chans.append(chan)
    return chans
