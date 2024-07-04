from rest_framework import serializers

from customuser.serializer import UserSerializer
from .models import Tag, Category, JournalEntry


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_name']


class JournalEntrySerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    tag = TagSerializer(many=True, read_only=True)
    tag_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    class Meta:
        model = JournalEntry
        fields = ['id', 'title, content, owner, category',, 'category_id', 'tag_id']
