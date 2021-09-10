from .base import InstantBaseTest

from instant.models import Channel


class InstantTestCreate(InstantBaseTest):
    def test_channels_creation(self):
        self.reset()
        chan = Channel.objects.create(name="chan")
        self.assertTrue(chan.is_active)
        self.assertEqual(chan.name, "$chan")
        self.assertEqual(chan.level, "superuser")
        self.assertEqual(str(chan), "$chan")

    def test_public_channel_creation(self):
        chan = Channel.objects.create(name="chan", level="public")
        self.assertEqual(chan.name, "chan")
        self.assertEqual(chan.level, "public")

    def test_channel_manager(self):
        Channel.objects.create(name="$chan")
        user_chans = Channel.objects.for_user(self.superuser)  #  type: ignore
        self.assertEqual(user_chans[0].name, "$chan")
        Channel.objects.create(name="chan", level="public")
        user_chans = Channel.objects.for_user(self.user)  #  type: ignore
        self.assertEqual(user_chans[0].name, "chan")
