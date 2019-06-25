from rest_framework import serializers
from .models import Profiles

class ProfileSerializerV1(serializers.ModelSerializer):
    class Meta:
        model = Profiles
        fields = "__all__"


    def create(self, validated_data):
        return Profiles.objects.create(**validated_data)    


