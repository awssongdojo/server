from django.shortcuts import HttpResponse
from .models import Song
from .models import SongManager
from django.core import serializers
import json


def index(req):
    songs = Song.objects.all()
    json_songs = serializers.serialize('json', songs)
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
