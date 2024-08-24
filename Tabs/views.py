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
  
    def get_permisson(self, request, *args, **kwargs):
        '''
        -Permission class for CRUD
        Restrict permisson to only creators for updates and delete 
        '''
        user = self.request.user
        tab_id = kwargs.get('tab')
        tab = Tabs.objects.filter(id=tab_id)
        
        if self.action in ['delete','update']:
            if user == tab.creator:
               return  [permissions.IsAuthenticated, permissions.IsOwner]
            else:
                raise  Exception('only creators can edit or delete tabs')
        return [permissions.IsAuthenticated]
                
        


    def perform_create(self, request, *args, **kwargs):
        user = self.request.user
        userprofile = User.objects.get(id=user.id)

        data = request.data.copy()
        data['creator'] = userprofile.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=self.request.user)
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