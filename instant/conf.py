# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User


USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', User)

USE_REVERSION=getattr(settings, 'MICROB_USE_REVERSION', "reversion" in settings.INSTALLED_APPS)

CODE_MODE = getattr(settings, 'MICROB_CODE_MODE', False)
CODEMIRROR_KEYMAP = getattr(settings, 'MICROB_CODEMIRROR_KEYMAP', 'default')

#MICROB_HITS_CHANNEL = getattr(settings, 'MICROB_HITS_CHANNEL', "$microb_hits")