from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, SAFE_METHODS
from .serializer import UserSerializer

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        permissions = []
        if self.request in SAFE_METHODS:
            permissions.append(IsAdminUser)
        return [permission() for permission in permissions]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer