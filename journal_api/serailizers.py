from rest_framework import serializers
from django.contrib.auth import get_user_model

from customuser.serializer import UserSerializer
from .models import Tag, Category, JournalEntry
import pdb


User = get_user_model()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'description']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'tag_name']
        extra_kwargs = {
            'tag_name': {'validators': []}
        }
    
    def validate(self, attrs):
        tag_name = attrs.get('tag_name', None)

        if self.instance:
            if Tag.objects.filter(tag_name=tag_name).exclude(id=self.instance.id).exists():
                raise serializers.ValidationError('This tag name already exists')
        else:
            if Tag.objects.filter(tag_name=tag_name).exists():
                raise serializers.ValidationError('This tag name already exists')

        return attrs
    
    def to_internal_value(self, data):
        if 'id' in data:
            try:
                instance = Tag.objects.get(id=data['id'])
                self.instance = instance
            except Tag.DoesNotExist:
                raise serializers.ValidationError("Tag with this id does not exist.")
        return super().to_internal_value(data)

class JournalEntrySerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), default=serializers.CurrentUserDefault(), source='user')
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    tags = TagSerializer(many=True, read_only=False)


    class Meta:
        model = JournalEntry
        fields = ['id', 'title', 'content', 'owner', 'category','category_id', 'tags']

    def create(self, validated_data):
        tags = validated_data.pop('tags', None)
        journal_entry = JournalEntry.objects.create(**validated_data)
        
        if tags is not None:
            for item in tags:
                tag_obj, created = Tag.objects.get_or_create(**item)
                journal_entry.tags.add(tag_obj)

        journal_entry.save()
        return journal_entry

    def update(self, instance, validated_data):
        print(validated_data)
        tags = validated_data.pop('tags', None)

        for key, value in validated_data.items():
            if hasattr(instance, key):
                setattr(instance, key, value)

        if tags or len(tags) == 0:
            print('executing')
            instance.tags.clear()
            for tag in tags:
                tag_obj, created = Tag.objects.get_or_create(**tag)
                instance.tags.add(tag_obj)

        instance.save()
        return instance