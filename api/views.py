from django.shortcuts import render
from .models import Home
from rest_framework import viewsets
from .serailizers import homeSerializaers

# Create your views here.
class HomeViewSet(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = homeSerializaers
