from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializer import UserSerializer

User = get_user_model()

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer