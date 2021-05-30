from django.conf import settings


CENTRIFUGO_API_KEY = getattr(settings, "CENTRIFUGO_API_KEY", None)
CENTRIFUGO_HMAC_KEY = getattr(settings, "CENTRIFUGO_HMAC_KEY", None)
CENTRIFUGO_HOST = getattr(settings, "CENTRIFUGO_HOST", "http://localhost")
CENTRIFUGO_PORT = getattr(settings, "CENTRIFUGO_PORT", 8000)

SITE_SLUG = getattr(settings, "SITE_SLUG", "site")
SITE_NAME = getattr(settings, "SITE_NAME", "Site")
