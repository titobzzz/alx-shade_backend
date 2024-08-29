from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from accounts.models import User
from Tabs.models import Tabs



# class TabCreationTest(APITestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(email="testuser@example.com", password="testpassword123")
#         self.client.login(email="testuser@example.com", password="testpassword123")

#     def test_create_tab(self):
#         url = reverse('tabs/') 
#         data = {
#             "text_content": "This is a test tab."
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertTrue(Tabs.objects.filter(text_content="This is a test tab.").exists())
