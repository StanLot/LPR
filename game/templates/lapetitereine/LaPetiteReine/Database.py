# Connect to database
import pymysql
from Class_Reine import *

# Function to select a statement and return a list
def select_statement(sql):
    statement = []
    db = pymysql.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="",  # your password
                         db="LaPetiteReine")        # name of the data base
    cur = db.cursor()
    cur.execute(sql)
    for row in cur.fetchall():
        statement.append(row)
    cur.close()
    db.close()

# Function to insert using a sql query
def insert_statement(sql,table):
    db = pymysql.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="",  # your password
                         db="LaPetiteReine")        # name of the data base

    cur = db.cursor()

    try:
        cur.execute(sql,table)
        db.commit()
    except:
        db.rollback()
    db.close()

def create_db():
    db = pymysql.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="",  # your password
                         db="LaPetiteReine")        # name of the data base
    cursor = db.cursor()

    #Structural tables
    cursor.execute("create table IF NOT EXISTS player (id_player int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(20), email varchar(70),password varchar(20),age int, profession varchar(20), date datetime)")
    cursor.execute("create table IF NOT EXISTS league (id_league int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(20), date datetime, name_creator varchar(20), total_player int DEFAULT 1, tour varchar(20), stage int DEFAULT 1)")
    cursor.execute("create table IF NOT EXISTS link_player_league (id_player_league int NOT NULL AUTO_INCREMENT PRIMARY KEY, name_player varchar(20), name_league varchar(20))")
    cursor.execute("create table IF NOT EXISTS cyclist (id_cyclist int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(20), surname varchar(20))")
    cursor.execute("create table IF NOT EXISTS link_player_league_cyclist (id_player_league_cyclist int NOT NULL AUTO_INCREMENT PRIMARY KEY, name_player varchar(20) , name_league varchar(20), name_cyclist varchar(20), selected boolean default 0)")

    #Race and results
    cursor.execute("create table IF NOT EXISTS tour (id_tour int NOT NULL AUTO_INCREMENT PRIMARY KEY, name varchar(20) , beginning datetime, end datetime)")
    cursor.execute("create table IF NOT EXISTS link_tour_cyclist (name_tour varchar(20), name_cyclist varchar(20))")
    cursor.execute("create table IF NOT EXISTS stage (id_stage int NOT NULL AUTO_INCREMENT PRIMARY KEY, name_tour varchar(20), val1 int , val2 int, val3 int, val4 int, val5 int, val6 int, val7 int, val8 int, val9 int, val10 int, val11 int, val12 int, val13 int, val14 int, val15 int, val16 int, val17 int, val18 int, val19 int, val20 int, yellow int, green int, white int, mountain int, date datetime)")

    #Betting rounds
    cursor.execute("create table IF NOT EXISTS bet (id_bet int NOT NULL AUTO_INCREMENT PRIMARY KEY, name_player varchar(20), name_league varchar(20), name_cyclist varchar(20), price int, stage int DEFAULT 1 ,date datetime )")



#Get the id ?
#Check if the name is already in the database ?
def insert_player(player):
    table = [player.name, player.email, player.password, player.age, player.profession]
    insert_statement("INSERT INTO player (name, email, password, age, profession) VALUES (%s, %s, %s, %s, %s)", table)

def insert_league(league):
    table = [league.name, league.creator, league.tour]
    insert_statement("INSERT INTO league (name, name_creator, tour) VALUES (%s, %s, %s)", table)

def insert_tour(tour):
    table = [tour.id_tour, tour.name]
    insert_statement("INSERT INTO tour (id_tour, name) VALUES (%s, %s)", table)

def insert_tour_cyclist(tour,cyclist):
    table = [tour.name, cyclist.name]
    insert_statement("INSERT INTO link_tour_cyclist (name_tour, name_cyclist) VALUES (%s, %s)", table)

def insert_player_league(player,league):
    table = [player.name, league.name]
    insert_statement("INSERT INTO link_player_league (name_player, name_league) VALUES (%s, %s)", table)

def insert_player_league_cyclist(player,league,cyclist):
    table = [player.name, league.name,cyclist.name]
    insert_statement("INSERT INTO link_player_league_cyclist (name_player, name_league, name_cyclist) VALUES (%s, %s, %s)", table)

def insert_bet(bet):
    table = [bet.player, bet.league,bet.cyclist,bet.price,bet.stage]
    insert_statement("INSERT INTO bet (name_player, name_league, name_cyclist, price,stage) VALUES (%s, %s, %s, %s, %s)", table)

#Check if it works...
def select_player_cyclist(player,league, stage):
    table = [player.name,league.name]
    select_statement("SELECT * FROM link_player_league_cyclist WHERE (name_player,name_league) VALUES (%s,%s)", table)

def select_selected_cyclist(player,league,stage):
    table = [player.name,league.name, int(1)]
    select_statement("SELECT * FROM link_player_league_cyclist WHERE (name_player,name_league,selected) VALUES (%s,%s,%s)", table)

def define_selected_cyclist(player,league,stage,cyclist):
    table = [player.name,league.name, cyclist.name]
    select_statement("UPDATE link_player_league_cyclist SET selected=1 WHERE (name_player,name_league,name_cyclist) VALUES (%s,%s,%s)", table)

def define_unselected_cyclist(player,league,stage,cyclist):
    table = [player.name,league.name, cyclist.name]
    select_statement("UPDATE link_player_league_cyclist SET selected=0 WHERE (name_player,name_league,name_cyclist) VALUES (%s,%s,%s)", table)

#Create function Delete after round1 ...
# create function to select cyclists
# Create bonus function
#To to
def count_selected_cyclist(player,league,stage,cyclist):
    select_selected_cyclist(player,league,stage)
