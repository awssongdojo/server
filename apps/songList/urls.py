from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
<<<<<<< HEAD
    path('add_playlist/', views.add_playlist)
=======
    path('get/<int:song_id>/', views.get),
    path('playlist/<int:other_id>/', views.playlist),
>>>>>>> e16282a80eee28dcf44075a96de8b76bfea48390
]