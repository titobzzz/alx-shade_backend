from rest_framework import serializers

from .models import *


class BallotSerializer(serializers.ModelSerializer):
    """
    Ballot serializer
    """
     

    class Meta:
        model = Ballots
        fields="__all__"        



class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields="__all__"

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = "__all__"

class TopicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topics
        fields = "__all__"
