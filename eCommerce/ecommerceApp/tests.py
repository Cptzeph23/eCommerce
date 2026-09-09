from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class AuthFlowTests(TestCase):
    def test_register_redirects_to_login_and_login_redirects_to_index(self):
        response = self.client.post(reverse('register_view'), {
            'username': 'alice',
            'email': 'alice@example.com',
            'password1': 'secret12345',
            'password2': 'secret12345',
        })

        self.assertRedirects(response, reverse('login_view'))
        self.assertEqual(User.objects.filter(username='alice').count(), 1)

        login_response = self.client.post(reverse('login_view'), {
            'username': 'alice',
            'password': 'secret12345',
        })

        self.assertRedirects(login_response, reverse('index'))
