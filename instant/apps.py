# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import json
from django.apps import AppConfig
from django.utils._os import safe_join
from django.template.loaders.app_directories import get_app_template_dirs

HANDLERS = {}
CHANNELS = {}
CHANNELS_NAMES = {}
DEFAULT_HANDLER = "instant/handlers/default.js"


class InstantConfig(AppConfig):
    name = 'instant'

    def ready(self):
        global HANDLERS, CHANNELS, CHANNELS_NAMES, DEFAULT_HANDLER
        from django.conf import settings
        debug = getattr(settings, "INSTANT_DEBUG", False)
        from .utils import get_channels_for_roles
        from .conf import ENABLE_STAFF_CHANNEL, ENABLE_USERS_CHANNEL, \
            ENABLE_SUPERUSER_CHANNEL
        col = '\033[91m'
        endcol = '\033[0m'
        if ENABLE_STAFF_CHANNEL is True:
            print(col + "Warning from Django Instant" + endcol + 
                  ": the setting ENABLE_STAFF_CHANNEL "
                  "will be deprecated in version 0.8. "
                  "Please use declarative channels instead")
        if ENABLE_USERS_CHANNEL is True:
            print(col + "Warning from Django Instant" + endcol + 
                  ": the setting ENABLE_USERS_CHANNEL "
                  "will be deprecated in version 0.8. "
                  "Please use declarative channels instead")
        if ENABLE_SUPERUSER_CHANNEL is True:
            print(col + "Warning from Django Instant" + endcol + 
                  ": the setting ENABLE_SUPERUSER_CHANNEL "
                  "will be deprecated in version 0.8. "
                  "Please use declarative channels instead")

        CHANNELS, CHANNELS_NAMES = get_channels_for_roles()
        try:
            if debug is True:
                print("Django Instant registered channels:")
                print(json.dumps(CHANNELS, indent=2))
        except AttributeError:
            pass
        # get channels handlers
        project_template_dirpaths = []
        # get default templates paths
        tconf = getattr(settings, "TEMPLATES", None)
        if tconf is not None:
            if "DIRS" in tconf[0]:
                for dir_ in tconf[0]["DIRS"]:
                    dirpath = safe_join(settings.BASE_DIR, dir_)
                    project_template_dirpaths.append(dirpath)
        # get modules templates paths
        modules_templatepaths = list(get_app_template_dirs("templates"))
        template_dirpaths = project_template_dirpaths + modules_templatepaths
        # get handlers directoriess
        for dir_ in template_dirpaths:
            if "instant" in os.listdir(dir_):
                idir = dir_ + "/instant"
                if "handlers" in os.listdir(idir):
                    hdir = idir + "/handlers"
                    for handler in os.listdir(hdir):
                        chan_name = handler.split(
                            "/")[-1:][0].replace(".js", "")
                        if dir_ not in project_template_dirpaths:
                            # the default handler must be in project dir
                            if handler != "default.js":
                                HANDLERS[chan_name] = hdir + "/" + handler
                        else:
                            if handler == "default.js":
                                DEFAULT_HANDLER = hdir + "/" + handler
                            else:
                                HANDLERS[chan_name] = hdir + "/" + handler
        if debug is True:
            print("Instant channels handlers found:")
            for handler in HANDLERS:
                print(handler + ": " + HANDLERS[handler])
            if DEFAULT_HANDLER is None:
                print("No default handler found")
            else:
                print("Default handler: " + DEFAULT_HANDLER)
            print()
