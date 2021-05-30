import jwt
import time
from .conf import CENTRIFUGO_HMAC_KEY


def connection_token(user):
    if CENTRIFUGO_HMAC_KEY is None:
        raise ValueError("Provide a CENTRIFUGO_HMAC_KEY in settings")
    claims = {"sub": user.username, "exp": int(time.time()) + 24 * 60 * 60}
    token = jwt.encode(claims, CENTRIFUGO_HMAC_KEY, algorithm="HS256")
    return token


def channel_token(client, channel):
    if CENTRIFUGO_HMAC_KEY is None:
        raise ValueError("Provide a CENTRIFUGO_HMAC_KEY in settings")
    claims = {
        "client": client,
        "channel": channel,
        "exp": int(time.time()) + 24 * 60 * 60,
    }
    token = jwt.encode(claims, CENTRIFUGO_HMAC_KEY, algorithm="HS256")
    return token
