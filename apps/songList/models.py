from django.db import models
from ..users.models import User


class SongManager(models.Manager):
    def validate(self, data):
        errors = []
        matching_song = Song.objects.filter(artist=data['artist'], title=data['title'])
        if matching_song:
            errors.append('Song aready in Database')
        if len(data['artist']) <2:
            errors.append('Artist name must be at least 2 Characters long')
        if len(data['title']) <2:
            errors.append('Title must be at least 2 Characters long')
        return errors

    def easy_create(self, data):
        user = User.objects.get(id=data['user_id'])
        return Song.objects.create(
            artist=data["artist"],
            title=data['title'],
            user=user,
        )     

class Song(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user =  models.ForeignKey(User, related_name="songs", on_delete=models.CASCADE)
    playlists = models.ManyToManyField(User, related_name="users")
    updated_at = models.DateTimeField(auto_now=True)
    objects = SongManager()


