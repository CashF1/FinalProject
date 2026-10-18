from django import forms
from .models import Player, Tournament

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ["first_name", "last_name", "email"]
        
class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ["name", "course", "date", "players"]
        widgets = {
            "date": forms.DateInput(attrs={"type": "date"}),
        }