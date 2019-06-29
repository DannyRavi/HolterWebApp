from rest_framework import serializers
from .models import Profiles


class ProfileSerializerV1(serializers.ModelSerializer):

    # docs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # doc =  DocsSerializer(write_only=True, required=False)
    # doc =  DocsSerializer(many=True, read_only=True)
    # user =  serializers.IntegerField(write_only=True)
    class Meta:
        model = Profiles
        fields = "__all__"

    
    def create(self, validated_data):
        # doc = validated_data.pop('docs')
        profile = Profiles.objects.create(**validated_data)
        # my_doc = Docs.objects.create(**doc,author=profile)
        return  profile


