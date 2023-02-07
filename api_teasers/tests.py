from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

class SetTeaserStatusApiTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.teaser_ids = [1, 2, 3]
        self.status = 'pending'
        self.user = User.objects.create_user(
            username='Q',
            password='q123'
        )

    def test_api_with_unauthenticated_user(self):
        response = self.client.post(
            reverse('set_teaser_status_api'),
            {'teaser_ids': self.teaser_ids, 'status': self.status}
        )
        self.assertEqual(response.status_code, 400)

class ObtainAuthTokenWithCSRFTokenTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
        username='Q', password='q123'
        )

    def test_can_obtain_token_and_csrf_token(self):
        response = self.client.post(reverse('api_token_auth'), {'username': 'Q', 'password': 'q123'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
        self.assertIn('csrftoken', response.cookies)

    def test_cannot_obtain_token_with_wrong_credentials(self):
        response = self.client.post(reverse('api_token_auth'), {'username': 'no_user', 'password': 'no_pass'})
        self.assertEqual(response.status_code, 400)
        self.assertNotIn('token', response.data)
        self.assertNotIn('csrftoken', response.cookies)
