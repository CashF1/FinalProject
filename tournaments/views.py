from django.shortcuts import render, get_object_or_404, redirect
from .models import Player
from .forms import PlayerForm

def home(request):
    return render(request, "tournaments/home.html")

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