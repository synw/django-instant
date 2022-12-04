from .base import InstantBaseTest

from instant.token import connection_token, channel_token


class InstantTestToken(InstantBaseTest):
    def test_connection_token(self):
        #with self.assertRaises(ValueError):
        #    with self.settings(CENTRIFUGO_HMAC_KEY=None):  
        #        connection_token(self.user)
        t = connection_token(self.user)
        # print(t)
        self.assertTrue(
            str(t).startswith(
                "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
            )
        )

    def test_channel_token(self):
        #with self.settings(CENTRIFUGO_HMAC_KEY=None) and self.assertRaises(ValueError):
        #    channel_token("chan", self.user)
        t = channel_token("chan", self.user)
        # print(t)
        self.assertTrue(
            str(t).startswith(
                (
                    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
                )
            )
        )
