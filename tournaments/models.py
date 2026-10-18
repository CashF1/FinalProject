from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tournament(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    date = models.DateField()
    players = models.ManyToManyField(Player, blank=True)
    
    def __str__(self):
        return self.name

class Score(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    strokes = models.PositiveIntegerField
    
    def __str__(self):
        return f"{self.player} - {self.tournament}: {self.strokes}"