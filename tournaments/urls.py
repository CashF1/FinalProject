from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("players/", views.player_list, name="player_list"),
     path("players/add/", views.player_create, name="player_create"),
    path("players/<int:player_id>/edit/", views.player_edit, name="player_edit"),
    path("players/<int:player_id>/delete/", views.player_delete, name="player_delete"),

]
