from rest_framework.views import APIView
from .serializers import SongSerializer,AlbumSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import Song,Album
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings


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
    
class SendEmail(APIView):
    permission_classes=[]
    def post(self,request,mail):
        try:
            email_template = 'LoginTemplate.html'  
            html_content = render_to_string(email_template)

            email = EmailMessage(
                body=html_content,
                to=[mail],
            )

            email.content_subtype = 'html'  

            email.send()

            return Response({'message': 'Email sent successfully!'}, status=status.HTTP_200_OK)


        except Exception as e:
            print(f'Error sending email: {str(e)}')
            return Response({"message":"Failed to send Email"}, status=status.HTTP_400_BAD_REQUEST)
        
class TestEmailTemplate(APIView):
    permission_classes =[]
    def get(self, request):
        try:
            html_content = render_to_string('LoginTemplate.html')

            return HttpResponse(html_content, content_type='text/html')

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


