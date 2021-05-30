# -*- coding: utf-8 -*-

def ensure_channel_is_private(chan):
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
