from django.test import TestCase, override_settings
from cent.core import generate_channel_sign
from .base import InstantBaseTest
from ..producers import _get_channel
from ..conf import PUBLIC_CHANNEL, SITE_SLUG, PUBLIC_CHANNELS
from ..utils import signed_response, _get_public_channel, _ensure_channel_is_private, \
    _check_chanconf, channels_for_role


class InstantTestUtils(InstantBaseTest):

    def test_get_public_channel(self):
        chan = _get_public_channel()
        self.assertEqual(chan, PUBLIC_CHANNEL)

    def test_signed_response(self):
        client = "client"
        chan = "test_chan"
        signature = generate_channel_sign(self.key, client, chan, info="")
        resp = signed_response(chan, client)
        self.assertEqual(resp, {"sign": signature})

    def test__ensure_channel_is_private(self):
        priv = _ensure_channel_is_private("$chan")
        self.assertEqual(priv, "$chan")
        priv = _ensure_channel_is_private("chan")
        self.assertEqual(priv, "$chan")

    def test_check_chanconf(self):
        """
        # settings:
        INSTANT_PUBLIC_CHANNELS=[
           ['test_site_public1'],
           ['test_site_public2'],
        ],
        """
        conf = _check_chanconf(PUBLIC_CHANNELS[0], False)
        res = dict(slug="test_site_public1", path=None)
        self.assertEqual(conf, res)

    def test_channels_for_role(self):
        """
        # settings:
        INSTANT_SUPERUSER_CHANNELS=[
            ["$test_site_admin1", ["/a/path", "/another/path"]],
            ['$test_site_admin2']
        ],
        INSTANT_STAFF_CHANNELS=[
            ["$test_site_staff1", ["/a/path"]],
            ['$test_site_staff2'],
        ],
        INSTANT_USERS_CHANNELS=[
            ['$test_site_users1'],
        ],
        INSTANT_PUBLIC_CHANNELS=[
            ['test_site_public1'],
            ['test_site_public2'],
        ],
        """
        chans, chans_names = channels_for_role("public")
        self.assertEqual(
            chans_names, [
                "test_site_public", "test_site_public1", "test_site_public2"])
        expected_chans = [
            dict(slug=PUBLIC_CHANNEL, path=None),
            dict(slug="test_site_public1", path=None),
            dict(slug="test_site_public2", path=None)
        ]
        self.assertEqual(chans, expected_chans)

        chans, chans_names = channels_for_role("users")
        self.assertEqual(chans_names, ["$test_site_users1"])
        expected_chans = [
            dict(slug="$test_site_users1", path=None)
        ]
        self.assertEqual(chans, expected_chans)

        chans, chans_names = channels_for_role("staff")
        self.assertEqual(
            chans_names, [
                "$test_site_staff1", "$test_site_staff2"])
        expected_chans = [
            dict(slug="$test_site_staff1", path=["/a/path"]),
            dict(slug="$test_site_staff2", path=None)
        ]
        self.assertEqual(chans, expected_chans)

        chans, chans_names = channels_for_role("superuser")
        self.assertEqual(
            chans_names, [
                "$test_site_admin1", "$test_site_admin2"])
        expected_chans = [
            dict(slug="$test_site_admin1", path=["/a/path", "/another/path"]),
            dict(slug="$test_site_admin2", path=None)
        ]
        self.assertEqual(chans, expected_chans)

    """
    @override_settings(INSTANT_ENABLE_PUBLIC_CHANNEL=False)
    def test_channels_for_role_no_defaults(self):
        # TOFIX
        chans, chans_names = channels_for_role("public")
        self.assertEqual(
            chans_names, [
                "test_site_public1", "test_site_public2"])
        expected_chans = [
            dict(slug="test_site_public1", path=None),
            dict(slug="test_site_public2", path=None)
        ]
        self.assertEqual(chans, expected_chans)"""
