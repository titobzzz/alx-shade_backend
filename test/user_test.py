from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from accounts.models import User

class UserRegistrationTest(APITestCase):
    def test_user_registration(self):
        url = reverse('user-register')  # Assuming the URL name is 'user-register'
        data = {
            "email": "testuser@example.com",
            "username": "testuser",
            "password": "testpassword123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="testuser@example.com").exists())
