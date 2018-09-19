# -*- coding: utf-8 -*-
from cent.core import generate_channel_sign
from .conf import PUBLIC_CHANNEL, SECRET_KEY, PUBLIC_CHANNELS, \
    USERS_CHANNELS, STAFF_CHANNELS, SUPERUSER_CHANNELS, ENABLE_PUBLIC_CHANNEL, \
    ENABLE_USERS_CHANNEL, ENABLE_STAFF_CHANNEL, ENABLE_SUPERUSER_CHANNEL, \
    DEFAULT_USERS_CHANNEL, DEFAULT_STAFF_CHANNEL, DEFAULT_SUPERUSER_CHANNEL


def warn(msg):
    col = '\033[91m'
    endcol = '\033[0m'
    print(col + "Warning from Django Instant" + endcol + ": " + msg)


def signed_response(channel, client):
    signature = generate_channel_sign(SECRET_KEY, client, channel, info="")
    return {"sign": signature}


def _get_public_channel():
    return PUBLIC_CHANNEL


def _ensure_channel_is_private(chan):
    if chan.startswith("$") is False:
        return "$" + chan
    return chan


def _check_chanconf(chanconf, private=True):
    chan = chanconf[0]
    if private is True:
        chan = _ensure_channel_is_private(chan)
    path = None
    if len(chanconf) > 1:
        path = chanconf[1]
    chan = dict(slug=chan, path=path)
    return chan


def channels_for_role(role):
    """
    Get the channels for a role
    """
    chans = []
    chans_names = []
    # default channels
    if role == "public":
        if ENABLE_PUBLIC_CHANNEL is True:
            chan = dict(slug=PUBLIC_CHANNEL, path=None)
            chans.append(chan)
            chans_names.append(PUBLIC_CHANNEL)
    elif role == "users":
        if ENABLE_USERS_CHANNEL is True:
            chan = _ensure_channel_is_private(DEFAULT_USERS_CHANNEL)
            chan = dict(slug=chan, path=None)
            chans.append(chan)
            chans_names.append(DEFAULT_USERS_CHANNEL)
    elif role == "staff":
        if ENABLE_STAFF_CHANNEL is True:
            chan = _ensure_channel_is_private(DEFAULT_STAFF_CHANNEL)
            chan = dict(slug=chan, path=None)
            chans.append(chan)
            chans_names.append(DEFAULT_STAFF_CHANNEL)
    elif role == "superuser":
        if ENABLE_SUPERUSER_CHANNEL is True:
            chan = _ensure_channel_is_private(DEFAULT_SUPERUSER_CHANNEL)
            chan = dict(slug=chan, path=None)
            chans.append(chan)
            chans_names.append(DEFAULT_SUPERUSER_CHANNEL)
    # declared channels
    if role == "public":
        if len(PUBLIC_CHANNELS) > 0:
            for chanconf in PUBLIC_CHANNELS:
                chan = _check_chanconf(chanconf, False)
                chans.append(chan)
                chans_names.append(chan["slug"])
    elif role == "users":
        if len(USERS_CHANNELS) > 0:
            for chanconf in USERS_CHANNELS:
                chan = _check_chanconf(chanconf)
                chans.append(chan)
                chans_names.append(chan["slug"])
    elif role == "staff":
        if len(STAFF_CHANNELS) > 0:
            for chanconf in STAFF_CHANNELS:
                chan = _check_chanconf(chanconf)
                chans.append(chan)
                chans_names.append(chan["slug"])
    elif role == "superuser":
        if len(SUPERUSER_CHANNELS) > 0:
            for chanconf in SUPERUSER_CHANNELS:
                chan = _check_chanconf(chanconf)
                chans.append(chan)
                chans_names.append(chan["slug"])
    return chans, chans_names


def get_channels_for_roles():
    chans = dict(public=[], users=[], staff=[], superuser=[])
    chans_names = chans.copy()
    roles = ["public", "users", "staff", "superuser"]
    for role in roles:
        ch, chn = channels_for_role(role)
        chans[role] = ch
        chans_names[role] = chn
    return chans, chans_names
