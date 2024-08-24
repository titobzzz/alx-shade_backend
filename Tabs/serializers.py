from rest_framework import serializers
from accounts.models import User
from .models import *

from accounts.serializer import *





class TabImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabImage
        fields = ['id', 'image']

class TabVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabVideo
        fields = ['id', 'video']


class TabSerializer(serializers.ModelSerializer):
    """
    Tab serializer
    """
    creator = UserSerializer(read_only=True)
    images = TabImageSerializer(many=True, required=False)
    videos = TabVideoSerializer(many=True, required=False)
     

    class Meta:
        model = Tabs
        fields="__all__"        
    
    def create(self, validated_data):
        # Extract nested data for images and videos
        images_data = validated_data.pop('images', [])
        videos_data = validated_data.pop('videos', [])

        # Create the Tab instance
        user = self.context['request'].user
        tab = Tabs.objects.create(creator=user, **validated_data)

        # Create related images
        for image_data in images_data:
            TabImage.objects.create(tab=tab, **image_data)

        # Create related videos
        for video_data in videos_data:
            TabVideo.objects.create(tab=tab, **video_data)

        return tab

    def update(self, instance, validated_data):
        # Update logic for images and videos
        images_data = validated_data.pop('images', [])
        videos_data = validated_data.pop('videos', [])

        # Update the Tab instance
        instance.text_content = validated_data.get('text_content', instance.text_content)
        instance.save()

        # Update images
        instance.images.all().delete()
        for image_data in images_data:
            TabImage.objects.create(tab=instance, **image_data)

      
        instance.videos.all().delete()  
        for video_data in videos_data:
            TabVideo.objects.create(tab=instance, **video_data)

        return instance


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
