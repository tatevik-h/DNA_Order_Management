from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User


class UserDetailViewTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.url = reverse('user-detail', args=[self.user.pk])

    def test_retrieve_user_detail(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'testuser')
        self.assertEqual(response.data['email'], 'testuser@example.com')

    def test_update_user_detail(self):
        self.client.force_authenticate(user=self.user)
        data = {'email': 'newemail@example.com'}
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'newemail@example.com')