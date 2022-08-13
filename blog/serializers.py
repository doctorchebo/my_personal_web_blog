from django.contrib.auth.models import Group
from rest_framework import serializers
from blog.models import Category, Comment, Post

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
    lookup_field = 'slug'
    class Meta:
        model = Post
        fields = ["id", "title", "slug", "image_url", "content", "created_at", "category"]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "author", "comment"]
        

