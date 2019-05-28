from django.shortcuts import HttpResponse
from .models import Song
from django.core import serializers
import json


def index(req):
    songs = Song.objects.all()
    json_songs = serializers.serialize('json', songs)
    return HttpResponse(json_songs, status=200, content_type='application/json')