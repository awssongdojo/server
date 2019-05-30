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
    def getAllSongs(self):
        song_list = Song.objects.all()
        data = {
            'songs': []
        }
        if song_list:
            for song in song_list:
                song_obj = {
                    'id': song.id,
                    'artist': song.artist,
                    'title': song.title,
                    'count': 0
                }
                playlists = Playlist.objects.filter(songs=song.id)
                if playlists:
                    count = 0
                    for entry in playlists:
                        count = count + entry.count
                    song_obj['count'] = count
                data['songs'].append(song_obj)
        return data

    def getSong(self, song_id):
        song_info = Playlist.objects.filter(songs=song_id)
        song = Song.objects.get(id=song_id)
        data = {
            'id': song.id,
            'title': song.title,
            'artist': song.artist,
            'users': []
        }
        if(song_info):
            for song in song_info:
                user = User.objects.get(id=song.users_id)
                user_obj = {
                    'id': user.id,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'count': song.count
                }
                data['users'].append(user_obj)
        return data

class Song(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user =  models.ForeignKey(User, related_name="songs", on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    objects = SongManager()

class Playlist(models.Model):
    songs =  models.ForeignKey(Song, related_name="playlist", on_delete=models.CASCADE)
    users =  models.ForeignKey(User, related_name="playlist", on_delete=models.CASCADE)
    count =  models.IntegerField()
    objects = SongManager()
