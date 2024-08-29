from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from accounts.models import User
from Tabs.models import Tabs, Polls

class PollCreationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", password="testpassword123")
        self.tab = Tabs.objects.create(creator=self.user, text_content="Sample tab")

    def test_create_poll(self):
        url = reverse('polls', kwargs={'tab_id': self.tab.id})
        data = {
            "name": "Sample Poll"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Polls.objects.filter(name="Sample Poll").exists())
