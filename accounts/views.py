from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import viewsets, mixins, exceptions
from rest_framework import permissions
from .models import *
from .serializer import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]
    

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegistrationSerializer
        if self.action == 'retrieve':
            return UserSerializer
        return super().get_serializer_class()
    
    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [permissions.AllowAny()]
    #     if self.action == 'list':
    #         return [permissions.IsAdminUser()]
    #     if self.action == 'retrieve':
    #         return [custom_permissions.IsOwnerOrReadOnly()]
    #     if self.action == 'patch':
    #         return [custom_permissions.IsOwnerOrReadOnly()]
    #     if self.action == 'destroy':
    #         return [permissions.IsAuthenticated(), permissions.IsAdminUser()]
        
    #     return super().get_permissions()

