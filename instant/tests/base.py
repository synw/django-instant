from django.test import TestCase
from django.conf import settings
from django.template import Context, Template


class InstantBaseTest(TestCase):

    def setUp(self):
        self.maxDiff = None
        self.key = getattr(settings, "CENTRIFUGO_SECRET_KEY")

    def debug(self, msg):
        print("\n----------------------------------------------")
        print(msg)
        print("----------------------------------------------")

    def render_template(self, string, context=None):
        context = context or {}
        context = Context(context)
        return Template(string).render(context)
