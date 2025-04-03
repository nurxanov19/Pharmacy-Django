from rest_framework import serializers
from .models import Medicine

class MediacineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'