from django.core.exceptions import ImproperlyConfigured
from cent.core import generate_channel_sign
from instant.conf import PUBLIC_CHANNEL, SECRET_KEY


def signed_response(channel, client):
    signature = generate_channel_sign(SECRET_KEY, client, channel, info="")
    return {"sign": signature}


def _get_public_channel():
    return PUBLIC_CHANNEL


def _ensure_channel_is_private(chanconf):
    print("CONF", chanconf)
    chan = chanconf[0][0]
    print("1", chanconf[0][0])
    if chan.startswith("$") is False:
        msg = "Channel " + chan + " must start with a $ to be considered private"
        raise ImproperlyConfigured(msg)
