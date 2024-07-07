from django.http import JsonResponse
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status

from .models import Tag, Category, JournalEntry
from .serailizers import TagSerializer, JournalEntrySerializer, CategorySerializer

class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class JournalEntryList(generics.ListCreateAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

class JournalEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer

    # def update(self, request, *args, **kwargs):
    #     tags = request.data.pop('tags', None)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data= request.data, many=False, partial=False)
    #     serializer.is_valid(raise_exception=True)

    #     if tags is not None:
    #         instance.tags.clear()
    #         for tag in tags:
    #             tag_obj, created = Tag.objects.get_or_create(**tag)
    #             instance.tags.add(tag_obj)
    #     return super().update(request, *args, **kwargs)