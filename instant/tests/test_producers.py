from cent import CentException

from .base import InstantBaseTest

from instant.producers import publish


class InstantTestProducers(InstantBaseTest):
    def test_publish(self):
        with self.settings(CENTRIFUGO_API_KEY=None) and self.assertRaises(ValueError):
            publish("chan")
        with self.assertRaises(CentException):
            publish("chan", "message")
        with self.assertRaises(CentException):
            publish(
                "chan",
                data={"foo": 1},
                event_class="important",
                bucket="testing",
            )
