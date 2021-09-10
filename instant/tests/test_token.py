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
                    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJteXVzZXIiLCJl"
                )
            )

    def test_channel_token(self):
        with self.assertRaises(ValueError):
            channel_token("cli", "chan")
        with self.settings(CENTRIFUGO_HMAC_KEY="key"):
            t = channel_token("cli", "chan")
            # print(t)
            self.assertTrue(
                str(t).startswith(
                    (
                        "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
                        "eyJjbGllbnQiOiJjbGkiLCJjaGFubmVsIjoiY2hhbiIsImV4cCI6"
                    )
                )
            )
