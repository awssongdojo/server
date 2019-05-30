from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add/', views.add),
    path('add_to_playlist/<int:songId>', views.add_playlist)
]