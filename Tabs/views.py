from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import (
    viewsets,
    permissions,
    status ,
    permissions)



from .models  import *

from .serializers import *


# Create your views here.

class TabViewSet(viewsets.ModelViewSet):

    queryset= Tabs.objects.all()
    serializer_class = TabSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    # def get_permsssions(self):


    def perform_create(self, request, *args, **kwargs):
        user = self.request.user
        userprofile = User.objects.get(id=user.id)

        data = request.data.copy()
        data['creator'] = userprofile.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




class CommentViewSet(viewsets.ModelViewSet):

    queryset= Comment.objects.all()
    serializer_class = TabSerializer
    # permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    # def get_permsssions(self):


    def create(self, request, *args, **kwargs):

        user = self.request.user

        self.request.data["creator"] = user.id
        serializer = CommentSerializer(data=self.request.data, context={'request': self.request, 'creator': user })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"error":"invalid form value"})
    

class PollsViewSet(viewsets.ModelViewSet):

    queryset = Polls.objects.all()
    serializer_class = PollSerializer


class Topic(viewsets.ModelViewSet):

    queryset = Topics.objects.all()
    serializer_class = TopicSerializer