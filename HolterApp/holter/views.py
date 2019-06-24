from django.shortcuts import render
from .models import Profiles
from .serializers import ProfileSerializerV1
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
# Create your views here.

# @csrf_exempt
class ProfileView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializerV1
    queryset = Profiles.objects.all()

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializerV1    