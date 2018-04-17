# -*- coding: utf-8 -*-


def get_role_channels(path, role):
    from .apps import CHANNELS
    if role == "all":
        role_chans = CHANNELS["public"] + CHANNELS["users"] + \
            CHANNELS["staff"] + CHANNELS["superuser"]
    else:
        role_chans = CHANNELS[role]
    chans = []
    if path.endswith("/"):
        path = path[:-1]
    for chan in role_chans:
        if chan["path"] is not None:
            for chanpath in chan["path"]:
                if chanpath.endswith("/"):
                    chanpath = chanpath[:-1]
                if chanpath == path:
                    chans.append(chan["slug"])
                    break
        else:
            chans.append(chan["slug"])
    return chans


def clean_chanpath(chanslug):
    name = chanslug
    name = name.replace("$", "")
    name = name.replace(":", "_")
    return name


def _ensure_channel_is_private(chan):
    name = chan
    if ":" in name:
        names = name.split(":")
        prefix = names[0]
        suffix = names[1]
        if suffix.startswith("$") is False:
            return prefix + ":$" + suffix
    else:
        if chan.startswith("$") is False:
            return "$" + chan
    return chan
