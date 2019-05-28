from django.db import models
from ..users.models import User


class SongManager(models.Manager):
    pass      

class Song(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user =  models.ForeignKey(User, related_name="songs", on_delete=models.CASCADE)
    playlists = models.ManyToManyField(User, related_name="users")
    updated_at = models.DateTimeField(auto_now=True)
    objects = SongManager()