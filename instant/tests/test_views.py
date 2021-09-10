from .base import InstantBaseTest

from django.urls import reverse
from django.http import JsonResponse, HttpResponseForbidden


class InstantTestViews(InstantBaseTest):
    def test_logout_view(self):
        self.client.login(username="myuser", password="password")
        response = self.client.get(reverse("instant-logout"))
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 200)
        self.client.logout()
        response = self.client.get(reverse("instant-logout"))
        self.assertIsInstance(response, HttpResponseForbidden)
        self.assertEqual(response.status_code, 403)

    def test_get_token(self):
        response = self.client.get(reverse("instant-get-token"))
        self.assertIsInstance(response, HttpResponseForbidden)
        # self.client.login(username="myuser", password="password")
        # response = self.client.get(reverse("instant-get-token"))
        # print("RESP", response)
