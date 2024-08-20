from rest_framework import serializers
from accounts.models import User
from .models import *

from accounts.serializer import *


class TabSerializer(serializers.ModelSerializer):
    """
    Tab serializer
    """
    creator = UserSerializer(read_only=True)
     

    class Meta:
        model = Tabs
        fields="__all__"        

    def create(self, validated_data):
        # Assuming the user is available via context (e.g., request.user)
        user = self.context['request'].user
        tab = Tabs.objects.create(creator=user, **validated_data)
        return tab


class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields="__all__"

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polls
        fields = "__all__"

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topics
        fields = "__all__"
