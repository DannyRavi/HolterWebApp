from django.shortcuts import render
from .models import Profiles
from .serializers import ProfileSerializerV1
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

# @csrf_exempt
class ProfileView(generics.ListCreateAPIView):
    serializer_class = ProfileSerializerV1
    queryset = Profiles.objects.all()
    permission_classes = (IsAuthenticated,)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfileSerializerV1
    