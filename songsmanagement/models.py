from django.db import models


    
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    coverimg = models.URLField()
    release_date = models.DateField()
    genre = models.CharField(max_length=50)


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    release_date = models.DateField()
    genre = models.CharField(max_length=50)
    link = models.URLField(default="https://example.com")

    def __str__(self):
        return self.title