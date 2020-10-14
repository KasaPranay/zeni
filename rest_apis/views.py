from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DBaseserializer
from .models import DBase

class DBaseViewSet(viewsets.ModelViewSet):
    queryset = DBase.objects.all().order_by('FirstName')
    serializer_class = DBaseserializer

