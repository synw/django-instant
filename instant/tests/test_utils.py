from .base import InstantBaseTest

from instant.init import ensure_channel_is_private


class InstantTestUtils(InstantBaseTest):
    def test_ensure_channel_is_private(self):
        name = ensure_channel_is_private("$chan")
        self.assertEqual(name, "$chan")
        name = ensure_channel_is_private("chan")
        self.assertEqual(name, "$chan")
        name = ensure_channel_is_private("ns:$chan")
        self.assertEqual(name, "ns:$chan")
        name = ensure_channel_is_private("ns:chan")
        self.assertEqual(name, "ns:$chan")
