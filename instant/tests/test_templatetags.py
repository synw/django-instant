import time
from cent.core import generate_token
from .base import InstantBaseTest


class InstantTestTemplatetags(InstantBaseTest):

    def test_get_centrifugo_url(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% get_centrifugo_url %}'
        )
        self.assertEqual(html, "http://localhost:8001")

    def test_debug_mode(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% debug_mode %}'
        )
        self.assertEqual(html, "false")

    def test_get_timestamp(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% get_timestamp %}'
        )
        ts = str(int(time.time()))
        self.assertEqual(html, ts)

    def test_mq_generate_token(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% mq_generate_token "username" "1529666693" %}'
        )
        token = generate_token(self.key, "username", "1529666693")
        self.assertEqual(html, token)

    def test_is_users_channel(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% is_users_channel %}'
        )
        uc = "False"
        self.assertEqual(html, uc)

    def test_get_users_channel(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% get_users_channel %}'
        )
        uc = '$test_site_users'
        self.assertEqual(html, uc)

    def test_is_staff_channel(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% is_staff_channel %}'
        )
        uc = "False"
        self.assertEqual(html, uc)

    def test_get_staff_channel(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% get_staff_channel %}'
        )
        uc = "$test_site_staff"
        self.assertEqual(html, uc)

    def test_is_superuser_channel(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% is_superuser_channel %}'
        )
        uc = "False"
        self.assertEqual(html, uc)

    def test_get_superuser_channel(self):
        html = self.render_template(
            '{% load instant_tags %}'
            '{% get_superuser_channel %}'
        )
        uc = "$test_site_admin"
        self.assertEqual(html, uc)
