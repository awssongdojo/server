from django.shortcuts import HttpResponse
from ..users.models import User
from .models import Song
from .models import Playlist
from .models import SongManager
from django.core import serializers
import json
from ..users.models import User


def index(req):
    songs = Song.objects.getAllSongs()
    json_songs = json.dumps(songs)
    print(json_songs)
    return HttpResponse(json_songs, status=200, content_type='application/json')

def add(req):
    post_data = json.loads(req.body.decode())
    errors = Song.objects.validate(post_data)
    if errors:
        return HttpResponse(json.dumps(errors), status=400, content_type='application/json')
    Song.objects.easy_create(post_data)
    songs = Song.objects.all()
    json_songs = serializers.serialize('json', songs)
    return HttpResponse(json_songs, status=200, content_type='application/json')

def add_playlist(req):
    post_data = json.loads(req.body.decode())
    print(post_data)
    song = Song.objects.get(id=post_data['song_id'])
    user = User.objects.get(id=post_data['user_id'])
    song.playlists.add(user)
    updated_song = Song.objects.get(id=post_data['song_id'])
    json_song = serializers.serialize('json', [updated_song])
    return HttpResponse(json_song, status=200, content_type='application/json')
def get(req, song_id):
    song = Playlist.objects.getSong(song_id)
    json_song = json.dumps(song)
    print(json_song)
    return HttpResponse(json_song, status=200, content_type='application/json')

def playlist(req, other_id):
    playlist = Playlist.objects.filter(users=other_id)
    json_playlist = serializers.serialize('json', playlist)
    return HttpResponse(json_playlist, status=200, content_type='application/json')

def add_playlist(req):
    post_data = json.loads(req.body.decode())
    song = Song.objects.get(id=post_data['song_id'])
    user = User.objects.get(id=post_data['user_id'])
    Playlist.objects.create(count='1', songs=song, users=user)
    songs = Song.objects.getAllSongs()
    json_songs = json.dumps(songs)
    return HttpResponse(json_songs, status=200, content_type='application/json')

def other(req, user_id):
    data = Playlist.objects.getPlaylist(user_id)
    print(data)
    data = json.dumps(data)
    print(data)
    return HttpResponse(data, status=200, content_type='application/json')
    

