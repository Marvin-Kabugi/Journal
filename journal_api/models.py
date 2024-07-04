from django.db import models
from django.conf import settings

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()


class JournalEntry(models.Model):
    title= models.CharField(max_length=500)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    published_date = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    tag_name = models.TextField()
    entry = models.ManyToManyField(JournalEntry)