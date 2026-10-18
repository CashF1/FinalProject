from django import forms
from .models import Player, Tournament, Score

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
            "players": forms.CheckboxSelectMultiple(),
        }
        
class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ["player", "tournament", "strokes"]