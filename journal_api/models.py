from django.db import models
from django.conf import settings
from django.utils import timezone

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)
    
class Tag(models.Model):
    tag_name = models.TextField(unique=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)

class JournalEntry(models.Model):
    title= models.CharField(max_length=500)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    published_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(default=timezone.now)


