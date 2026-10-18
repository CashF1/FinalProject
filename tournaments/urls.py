from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("players/", views.player_list, name="player_list"),
    path("players/add/", views.player_create, name="player_create"),
    path("players/<int:player_id>/edit/", views.player_edit, name="player_edit"),
    path("players/<int:player_id>/delete/", views.player_delete, name="player_delete"),
    path("tournaments/", views.tournament_list, name="tournament_list"),
    path("tournaments/add/", views.tournament_create, name="tournament_create"),
    path("tournaments/<int:tournament_id>/edit/", views.tournament_edit, name="tournament_edit"),
    path("tournaments/<int:tournament_id>/delete/", views.tournament_delete, name="tournament_delete"),
    path("scores/", views.score_list, name = "score_list"),
    path("scores/add/", views.score_create, name="score_create"),
]
