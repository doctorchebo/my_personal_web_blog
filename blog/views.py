from django.contrib.auth.models import Group
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CategorySerializer, PostSerializer, GroupSerializer
from .models import Category, Comment, Post

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated] 
    lookup_field = 'slug'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated] 

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated] 


def home(request):
    return render(request, 'home.html')