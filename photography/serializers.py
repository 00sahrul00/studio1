from rest_framework import serializers
from .models import Studio, Photographer, Photoshoot

# buat kelas serializer
class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

class PhotographerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photographer
        fields = '__all__'

class PhotoshootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photoshoot
        fields = '__all__'