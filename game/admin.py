from django.contrib import admin
from .models import League, Link_user_league, Tour, List_cyclist_tour, Link_user_league_cyclist, Stage, Result, Bet, Cyclist

admin.site.register(League)
admin.site.register(Link_user_league)
admin.site.register(Tour)
admin.site.register(List_cyclist_tour)
admin.site.register(Link_user_league_cyclist)
admin.site.register(Stage)
admin.site.register(Result)
admin.site.register(Bet)
admin.site.register(Cyclist)
