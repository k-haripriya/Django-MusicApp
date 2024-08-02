from rest_framework import serializers
from .models import Song,Album

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'  

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__' 
