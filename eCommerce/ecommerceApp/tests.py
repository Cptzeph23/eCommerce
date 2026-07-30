from django.test import TestCase
from django.urls import reverse

from .models import NewUser


class IndexViewTests(TestCase):
    def test_successful_login_redirects_to_index_page(self):
        NewUser.objects.create(email='user@example.com', password='secret123')

        response = self.client.post(reverse('index'), {
            'email': 'user@example.com',
            'password': 'secret123',
        })

        self.assertRedirects(response, reverse('index'))
