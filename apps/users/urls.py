from django.urls import path
from . import views

urlpatterns = [
    path('show_all_users/', views.show_all_users),
    path('show/<int:user_id>/', views.show),
    path('create/', views.create),
    path('login/', views.login),
]