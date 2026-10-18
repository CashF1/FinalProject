from django.shortcuts import render, get_object_or_404, redirect
from .models import Player, Tournament, Score
from .forms import PlayerForm, TournamentForm, ScoreForm

def home(request):
    return render(request, "tournaments/home.html")

#Player CRUD

def player_list(request):
    players = Player.objects.all()
    return render(request, "tournaments/player_list.html", {"players": players})

def player_create(request):
    if request.method=="POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("player_list")
    else:
        form = PlayerForm()
        
    return render(request, "tournaments/player_form.html", {
        "form": form,
        "title": "Add Player"
    })
        
def player_edit(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    
    if request.method == "POST":
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect("player_list")
    else:
        form = PlayerForm(instance=player)
    return render(request, "tournaments/player_form.html", {
        "form": form,
        "title": "Edit Player"
    })
    
def player_delete(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    
    if request.method == "POST":
        player.delete()
        return redirect("player_list")
    
    return render(request, "tournaments/player_confirm_delete.html", {
        "player": player
    })
    
#Tournament CRUD

def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, "tournaments/tournament_list.html", {"tournaments": tournaments})

def tournament_create(request):
    if request.method=="POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tournament_list")
    else:
        form = TournamentForm()
        
    return render(request, "tournaments/tournament_form.html", {
        "form": form,
        "title": "Create Tournament"
    })
        
def tournament_edit(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    
    if request.method == "POST":
        form = TournamentForm(request.POST, instance=tournament)
        if form.is_valid():
            form.save()
            return redirect("tournament_list")
    else:
        form = TournamentForm(instance=tournament)
    return render(request, "tournaments/tournament_form.html", {
        "form": form,
        "title": "Edit Tournament"
    })

def tournament_delete(request, tournament_id):
    tournament = get_object_or_404(Tournament, id=tournament_id)
    
    if request.method == "POST":
        tournament.delete()
        return redirect("tournament_list")
    
    return render(request, "tournaments/tournament_confirm_delete.html", {
        "tournament": tournament
    })
    
#Score CRUD

def score_list(request):
    scores = Score.objects.select_related("player", "tournament").order_by("strokes")
    
    return render(request, "tournaments/score_list.html", {"scores": scores})

def score_create(request):
    tournament_id = request.GET.get("tournament")
    
    tournaments = Tournament.objects.all()
    scores = Score.objects.select_related("player","tournament").order_by("strokes")
    
    if tournament_id:
        scores = scores.filter(tournament_id=tournament_id)
        
    return render(request, "tournaments/score_list.html", {
        "scores": scores,
        "tournaments": tournaments,
        "selected_tounament": tournament_id
    })