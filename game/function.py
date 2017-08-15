import string
import random
from game.models import *

#Calculate the remaining money of a user
def calculate_money(user_id,league_id,stage):
    from game.models import Bet, Link_user_league
    list_of_bet = Bet.objects.filter(id_user_id =user_id,id_league_id = league_id, stage = stage)
    total_money = Link_user_league.objects.get(id_league_id=league_id,id_user_id=user_id).money
    for bet in list_of_bet:
        total_money = total_money - bet.price
    return(total_money)

# Create an Id for each league to allow people to subscribe
def id_generator():
    return(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15)))

# Define a list with all the cyclist people has bet on (cyclist appears once even if 2 bets)
def find_cyclist(list_of_bet):
    list_of_cyclist = []
    for bet in list_of_bet:
        if bet.id_cyclist_id not in list_of_cyclist:
            list_of_cyclist.append(bet.id_cyclist_id)
    return(list_of_cyclist)

def find_cyclist_excluding_bought(list_of_cyclist,list_of_bet):
    #Very dirty function
    from game.models import Cyclist
    list_of_id_cyc = []
    list_of_id_bet = []
    for cyclist in list_of_cyclist:
        list_of_id_cyc.append(cyclist.id)
    for bet in list_of_bet:
        list_of_id_bet.append(bet.id_cyclist_id)
    list_of_cyc = []
    for cyc in list_of_id_cyc:
        if cyc not in list_of_id_bet:
            cyclist = Cyclist.objects.get(id = cyc)
            list_of_cyc.append(cyclist)
    return(list_of_cyc)

# Define function to understand if a bet is legitimate or not
def good_bet(link_user_league_id, price, cyclist_id,user_id,league_id,stage):
    from game.models import Cyclist, Link_user_league, Bet, Link_user_league_cyclist
    cyclist = Cyclist.objects.get(id = cyclist_id)
    link_user_league = Link_user_league.objects.get(id = link_user_league_id)
    money = calculate_money(user_id,league_id,stage)
    #test_bet = Bet.objects.filter(id_user_id=user_id,id_league_id=league_id,stage=stage)
    #test_exist = Link_user_league_cyclist.objects.filter(id_user_id=user_id,id_league_id=league_id,id_cyclist_id=cyclist_id)
    if money <= price:
        return(False)
    if price < cyclist.salary:
        return(False)
    else:
        return(True)

def calculate_point(user_id,league_id,tour_id):
    from django.db import models
    from game.models import Link_user_league_cyclist, Result
    list_of_cyclist = Link_user_league_cyclist.objects.filter(id_user_id=user_id,id_league_id=league_id)
    point = 0
    for cyclist in list_of_cyclist:
        list_of_res = Result.objects.filter(id_cyclist_id = cyclist.id_cyclist_id,id_tour_id = tour_id)
        for res in list_of_res:
            point = point + res.point
    return(point)

def calculate_point_cyc(cyclist_id,tour_id):
    from django.db import models
    from game.models import Result
    point = 0
    list_of_res = Result.objects.filter(id_cyclist_id = cyclist_id,id_tour_id = tour_id)
    for res in list_of_res:
        point = point + res.point
    return(point)

def add_dict(mydict,key,money):
    if key in mydict:
        mydict[key] += money
    else:
        mydict[key] = money
    return(mydict)
