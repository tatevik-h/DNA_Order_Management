from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class SignupViewTests(APITestCase):

    def test_signup_with_valid_data(self):
        url = reverse('signup')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_signup_with_invalid_data(self):
        url = reverse('signup')
        data = {
            'username': '',
            'email': 'testuserexample.com',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)