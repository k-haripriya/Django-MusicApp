from rest_framework.views import APIView
from .serializers import SongSerializer,AlbumSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Song,Album


class CreateAlbum(APIView):
    def post(self,request):
        serializer = AlbumSerializer(data=request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = AlbumSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetAllAlbums(APIView):
    def get(self,request):
        songs = Album.objects.all()
        serializer = AlbumSerializer(songs,many=True)
        return Response(serializer.data)

class CreateSongs(APIView):
    def post(self,request):
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = SongSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GetAlbumSongs(APIView):
    def get(self,request,albumid):
        try:
            album = Album.objects.get(pk=albumid)
            albumserializer = AlbumSerializer(album)
        except Album.DoesNotExist:
            return Response({"message:": "Album Does not Exist"}, status=status.HTTP_404_NOT_FOUND)
        

        songs = Song.objects.filter(id=albumid)
        serializer = SongSerializer(songs,many=True)
        return Response({"content":{"album":albumserializer.data,"songs":serializer.data}})

