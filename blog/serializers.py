from django.contrib.auth.models import Group
from rest_framework import serializers
from blog.models import Category, Post

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]

class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    class Meta:
        model = Post
        fields = ["id", "title", "image", "content", "created_at", "category"]

