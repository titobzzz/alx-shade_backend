from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from accounts.models import User

class UserAuthenticationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", password="testpassword123")

    def test_user_login(self):
        url = reverse('accounts/auth/login')  
        data = {
            "email": self.user.email,
            "password": "testpassword123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
