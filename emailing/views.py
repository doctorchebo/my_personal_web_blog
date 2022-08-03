from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ContactMeSerializer
from .models import ContactMe

class ContactMeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that saves contact information from the contactMe form
    """
    queryset = ContactMe.objects.all().order_by('-created_at')
    serializer_class = ContactMeSerializer
    permission_classes = [permissions.AllowAny]
