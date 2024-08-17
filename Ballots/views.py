from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, mixins, permissions
from rest_framework import permissions


from .models  import *

from .serializers import *


# Create your views here.

class BallotViewSet(viewsets.ModelViewSet):

    queryset= Ballots.objects.all()
    serializer_class = BallotSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    # def get_permsssions(self):


    def create(self, request, *args, **kwargs):
        user = request.user

        data = dict(request.data)
        data["creator"] = user.id
        serializer = BallotSerializer(data=data, context={'request': self.request, 'creator': user, })
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data)
        return Response({"error":"invalid form value"})



class CommentViewSet(viewsets.ModelViewSet):

    queryset= Comment.objects.all()
    serializer_class = BallotSerializer
    permission_classes = [permissions.IsAuthenticated]
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

    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class Topic(viewsets.ModelViewSet):

    queryset = Topics.objects.all()
    serializer_class = TopicSerializer