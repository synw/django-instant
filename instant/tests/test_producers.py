from django.test import TestCase
from .base import InstantBaseTest
from ..producers import _get_channel, publish
from ..conf import PUBLIC_CHANNEL, SITE_SLUG


class InstantTestProducers(InstantBaseTest):

    def test_get_channel(self):
        chan = _get_channel(None, None)
        self.assertEqual(chan, PUBLIC_CHANNEL)
        chan = _get_channel(None, "users")
        self.assertEqual(chan, "$" + SITE_SLUG + '_users')
        chan = _get_channel(None, "superuser")
        self.assertEqual(chan, "$" + SITE_SLUG + '_admin')
        chan = _get_channel(None, "staff")
        self.assertEqual(chan, "$" + SITE_SLUG + '_staff')
        chan = _get_channel("chan", "users")
        self.assertEqual(chan, "chan")

    """
    # TOFIX
    def test_producers_settings(self):
        err = publish("Test message")
        self.assertEqual(err, None)
        with self.settings(INSTANT_BROADCAST_WITH="go"):
            from django.conf import settings
            from ..conf import BROADCAST_WITH
            self.debug(BROADCAST_WITH)
            self.debug(settings.INSTANT_BROADCAST_WITH)
            err = publish("Test message")
            self.assertEqual(err, None)
    """