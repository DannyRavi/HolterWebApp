from rest_framework import serializers
from .models import Profiles
import re
from rest_framework.exceptions import ValidationError
from doc.serializers import DocsSerializer
from django.contrib.auth.models import User
from doc.models import Docs
from django.shortcuts import get_object_or_404

class ProfileSerializerV1(serializers.ModelSerializer):

    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    post = DocsSerializer(write_only=True, required=False)
    user = serializers.IntegerField(write_only=True)
    class Meta:
        model = Profiles
        fields = "__all__"

    
    def create(self, validated_data):
        if 'doc' in validated_data:
            user = validated_data.pop('user')
            user = get_object_or_404(User, pk=user)
            post = validated_data.pop('doc')
            profile = Profiles.objects.create(user=user, **validated_data)
            my_post = Docs.objects.create(**post, author=profile)
        else:
            user = validated_data.pop('user')
            user = get_object_or_404(User, pk=user)
            profile = Profiles.objects.create(user=user, **validated_data)

        return profile


