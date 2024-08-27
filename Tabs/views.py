from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import (
    viewsets,
    permissions,
    status ,
    permissions)



from .models  import *

from .serializers import *

from custom import custumpermisons
from rest_framework.exceptions import PermissionDenied

from rest_framework.parsers import MultiPartParser, FormParser


# Create your views here.

class TabViewSet(viewsets.ModelViewSet):
    queryset = Tabs.objects.all()
    serializer_class = TabSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)
    lookup_field = 'pk'

    def get_permissions(self):
        '''
        Permission class for CRUD
        Restrict permission to only creators for updates and delete 
        '''
        user = self.request.user
        tab_id = self.kwargs.get('pk')  
        tab = Tabs.objects.filter(id=tab_id).first()
        
        if self.action in ['destroy', 'update']: 
            if tab and user == tab.creator:
                return [permissions.IsAuthenticated(),  custumpermisons.IsOwner()]
            else:
                raise PermissionDenied('Only creators can edit or delete tabs')
        
        return [permissions.IsAuthenticated()]



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