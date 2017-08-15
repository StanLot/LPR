import datetime


# Account for each people who join the game
class Player:

    list_of_cyclist =[]
    list_of_league = []

    def __init__(self, name, email, password, age, profession):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        self.profession = profession
        self.date = datetime.datetime.now().day

    def add_cyclist(self, cyclist):
        self.list_of_cyclist.append(cyclist)

    def calculate_point(self,list_of_cyclist):
        for i in self.list_of_cyclist:
            current_points = current_points + i.point
        return(current_points)


class League:

    list_players = []
    list_bet = []
    list_potential_cyclist = []

    def __init__(self, name, player,tour):
        self.name = name
        self.creator = player.name
        self.tour = tour.name
        self.creation_date = datetime.datetime.now().day

    def add_player(self, league_player):
        self.list_players.append(league_player)


    def make_bet(cyclist,price,list_of_cyclist):
        bet = Bet(player,cyclist,price)

class Tour:

    list_of_cyclist = []
    #THe id is built using the year and the number of the tour 1, 2 or 3
    def __init__(self,name,id_tour):
        self.name = name
        self.id_tour = id_tour

# Iteration of a player inside a list

class Bet:
    def __init__(self,player,league,cyclist,price,stage):
        self.player = player.name
        self.cyclist = cyclist.name
        self.league = league.name
        self.price = price
        self.stage = stage



class Cyclist:
    def __init__(self, name, point):
        self.name = name
        self.point = 0
