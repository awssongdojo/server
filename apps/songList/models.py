from django.db import models
from ..users.models import User
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class SongManager(models.Manager):
    pass      

class Song(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user =  models.ForeignKey(User, related_name="songs", on_delete=models.CASCADE)
    playlists = models.ManyToManyField(User, related_name="users")
    updated_at = models.DateTimeField(auto_now=True)
    objects = SongManager()