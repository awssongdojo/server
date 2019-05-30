from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('add_playlist/', views.add_playlist),
    path('get/<int:song_id>/', views.get),
    path('playlist/<int:other_id>/', views.playlist),
]