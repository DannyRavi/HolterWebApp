from rest_framework import serializers
from .models import Docs




class DocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docs
        fields = "__all__"

    
    def create(self, validated_data):
        doc = Docs.objects.create(**validated_data)
        return  doc
