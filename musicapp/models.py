from django.db import models
from datetime import datetime

# Create your models here.


class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()

    def __init__(self):
        pass


class Song(models.Model):
    associated_artiste = models.ForeignKey(Artiste, on_delete=models.CASCADE)

    title = models.CharField(max_length=400)
    date_released = models.DateField()
    likes = models.IntegerField()
    artiste_id = models.CharField(max_length=10)

    def __init__(self):
        pass


class Lyrics(models.Model):

    associated_song = models.ForeignKey(Song, on_delete=models.CASCADE)

    content = models.CharField(max_length=1000)
    song_id = models.CharField(max_length=10)

    def __init__(self):
        pass
