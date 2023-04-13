from rest_framework import serializers
from .models import PhotoModel

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = '__all__'