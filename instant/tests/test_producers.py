from cent import CentException

from .base import InstantBaseTest

from instant.producers import publish


class InstantTestProducers(InstantBaseTest):
    def test_publish(self):
        with self.assertRaises(ValueError):
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
