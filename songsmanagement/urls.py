from django.urls import path,include
from .views import CreateSongs,GetAlbumSongs,CreateAlbum,GetAllAlbums,TestEmailTemplate,SendEmail

urlpatterns = [
    path('addalbum/',CreateAlbum.as_view(),name="Create-Album"),
    path('getAllalbums/',GetAllAlbums.as_view(),name="GetAll-Album"),
    path("addsong/",CreateSongs.as_view(),name="Create-songs"),
    path('getalbumsongs/<int:albumid>',GetAlbumSongs.as_view(),name="GetAllsongs"),
    path('testtemplate/',TestEmailTemplate.as_view(),name="Test-template"),
    path('sendMail/<str:mail>',SendEmail.as_view(),name='email')
]
