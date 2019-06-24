from django.shortcuts import render
from .models import Profiles
from .serializers import ProfileSerializerV1
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ProfileView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializerV1
    queryset = Profiles.objects.all()