from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from users.models import User


class UserDeactivateViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@example.com',
            password='testpassword'
        )
        self.url = reverse('user_deactivate', args=[self.user.pk])

    def test_deactivate_user(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(User.objects.get(pk=self.user.pk).is_active)
