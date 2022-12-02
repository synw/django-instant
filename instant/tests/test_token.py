from .base import InstantBaseTest

from instant.token import connection_token, channel_token


class InstantTestToken(InstantBaseTest):
    def test_connection_token(self):
        with self.assertRaises(ValueError):
            connection_token(self.user)
        with self.settings(CENTRIFUGO_HMAC_KEY="key"):
            t = connection_token(self.user)
            # print(t)
            self.assertTrue(
                str(t).startswith(
                    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
                )
            )

    def test_channel_token(self):
        with self.assertRaises(ValueError):
            channel_token("cli", "chan")
        with self.settings(CENTRIFUGO_HMAC_KEY="key"):
            t = channel_token("cli", "chan")
            # print(t)
            self.assertTrue(
                str(t).startswith(
                    (
                        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
                    )
                )
            )
