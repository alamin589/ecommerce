from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Group
from .serielzers import GroupSerializer
class GroupViewset(viewsets.ModelViewSet):
   queryset = Group.objects.all()
   serializer_class = GroupSerializer 