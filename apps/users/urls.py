from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_all_users),
    path('<int:user_id>', views.show),
    path('<int:user_id>/playlist', views.user_playlist),
    path('create/', views.create),
    path('login/', views.login),
]