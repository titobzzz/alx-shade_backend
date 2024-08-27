from rest_framework import serializers
from accounts.models import User
from .models import *

from accounts.serializer import *

class HashTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ['id', 'name']


class TabMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TabMedia
        fields = ['id', 'media_type', 'file']

class TabSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    media = TabMediaSerializer(many=True, required=False)

    class Meta:
        model = Tabs
        fields = "__all__"

    def create(self, validated_data):
        media_data = self.context['request'].FILES.getlist('media')
        tags_data = validated_data.pop('tag', [])
        
        user = self.context['request'].user
        tab = Tabs.objects.create(creator=user, **validated_data)
        
        if tags_data:
            tags = [Topics.objects.get_or_create(name=tag['name'])[0] for tag in tags_data]
            tab.tag.set(tags)
        
        for media_file in media_data:
            media_type = 'image' if media_file.content_type.startswith('image') else 'video'
            TabMedia.objects.create(tab=tab, file=media_file, media_type=media_type)
        
        return tab

    def update(self, instance, validated_data):
        media_data = validated_data.pop('media', [])
        tags_data = validated_data.pop('tag', [])

        instance.text_content = validated_data.get('text_content', instance.text_content)
        instance.save()

        tags = []
        for tag_name in tags_data:
            tag, created = Topics.objects.get_or_create(name=tag_name)
            tags.append(tag)
        instance.tag.set(tags)

        instance.media.all().delete()
        for media_item in media_data:
            TabMedia.objects.create(tab=instance, **media_item)

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
