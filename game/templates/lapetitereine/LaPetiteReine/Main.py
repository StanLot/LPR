from Database import *
from Class_Reine import *
import django


create_db()

Froome = Cyclist("Froome",200)
Stan = Player("Stan","mail","password",24,"glandeur")
Vuelta17 = Tour("Vuelta 2017",20173)
Compet = League("Saganators",Stan,Vuelta17)
Ench1 = Bet(Stan,Compet,Froome,200,1)

insert_player(Stan)
insert_league(Compet)
insert_tour(Vuelta17)
insert_tour_cyclist(Vuelta17,Froome)
insert_player_league(Stan,Compet)
insert_player_league_cyclist(Stan,Compet,Froome)
insert_bet(Ench1)
