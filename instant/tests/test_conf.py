from typing import Any, Dict
from .base import InstantBaseTest

from instant.init import generate_settings_from_conf
from instant.conf import (
    CENTRIFUGO_API_KEY,
    CENTRIFUGO_HMAC_KEY,
    CENTRIFUGO_HOST,
    CENTRIFUGO_PORT,
    SITE_SLUG,
    SITE_NAME,
)


class InstantTestConf(InstantBaseTest):
    def test_default_conf(self):
        self.assertEqual(CENTRIFUGO_API_KEY, None)
        self.assertEqual(CENTRIFUGO_HMAC_KEY, None)
        self.assertEqual(CENTRIFUGO_HOST, "http://localhost")
        self.assertEqual(CENTRIFUGO_PORT, 8000)
        self.assertEqual(SITE_SLUG, "site")
        self.assertEqual(SITE_NAME, "Site")

    def test_generate_settings_from_conf(self):
        conf: Dict[str, Any] = {"token_hmac_secret_key": "key", "api_key": "key"}
        s = generate_settings_from_conf(conf, "site")
        self.assertListEqual(
            [
                'CENTRIFUGO_HOST = "http://localhost"',
                "CENTRIFUGO_PORT = 8427",
                'CENTRIFUGO_HMAC_KEY = "key"',
                'CENTRIFUGO_API_KEY = "key"',
                'SITE_NAME = "site"',
            ],
            s,
        )
        s = generate_settings_from_conf(conf)
        self.assertListEqual(
            [
                'CENTRIFUGO_HOST = "http://localhost"',
                "CENTRIFUGO_PORT = 8427",
                'CENTRIFUGO_HMAC_KEY = "key"',
                'CENTRIFUGO_API_KEY = "key"',
                'SITE_NAME = "tests"',
            ],
            s,
        )
