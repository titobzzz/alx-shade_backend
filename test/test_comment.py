from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from accounts.models import User
from Tabs.models import Tabs, Comment

class CommentCreationTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="testuser@example.com", password="testpassword123")
        self.tab = Tabs.objects.create(creator=self.user, text_content="Sample tab")

    def test_create_comment(self):
        url = reverse('comments', kwargs={'tab_id': self.tab.id})
        data = {
            "content": "This is a test comment."
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Comment.objects.filter(content="This is a test comment.").exists())
