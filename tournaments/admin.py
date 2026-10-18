from django.contrib import admin
from .models import Player, Tournament, Score

admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(Score)