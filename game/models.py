from django.db import models
from django.utils import timezone
import datetime
from django import forms
from django.forms import ModelForm
import django_tables2 as tables
from game.function import *

class League(models.Model):
    name = models.CharField(max_length=50)
    id_creator = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    id_tour = models.ForeignKey('Tour', on_delete=models.CASCADE)
    step = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)
    reference = models.CharField(max_length=20,default=id_generator())
    def __str__(self):
        return self.name

class LeagueForm(forms.ModelForm):
   class Meta:
     model = League
     fields = ['name']

#Just to allow subscription
class Join(models.Model):
    reference = models.CharField(max_length=30)
    creation_date = models.DateTimeField(default=timezone.now)

class JoinForm(forms.ModelForm):
   class Meta:
     model = Join
     fields = ['reference']

class Link_user_league(models.Model):
    id_user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    id_league = models.ForeignKey('League',on_delete=models.CASCADE)
    money = models.IntegerField(default=30000000)
    creation_date = models.IntegerField(default=0)
    def __str__(self):
        return(str(self.id_league)+' /' + str(self.id_user))


class Link_user_leagueTable(tables.Table):

    class Meta:
        model = Link_user_league
        # add class="paleblue" to <table> tag
        exclude = ('id','id_league','money','creation_date' )

class Tour(models.Model):
    name = models.CharField(max_length=50)
    creation_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name

class List_cyclist_tour(models.Model):
    id_tour = models.ForeignKey('Tour',on_delete=models.CASCADE)
    id_cyclist = models.ForeignKey('Cyclist',on_delete=models.CASCADE)
    creation_date = models.DateTimeField(default=timezone.now)

class Link_user_league_cyclist(models.Model):
    id_league = models.ForeignKey('League',on_delete=models.CASCADE)
    id_user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    id_cyclist = models.ForeignKey('Cyclist',on_delete=models.CASCADE)
    selected = models.IntegerField(default=0)
    point = models.IntegerField(default=0)

class Link_user_league_cyclistTable(tables.Table):
    class Meta:
        model = Link_user_league_cyclist
        # add class="paleblue" to <table> tag
        exclude = ('id','id_league','id_user' )

#Useless for the moment
class Stage(models.Model):
    id_tour = models.ForeignKey('League',on_delete=models.CASCADE)
    date = models.DateTimeField()

class Result(models.Model):
    id_tour = models.ForeignKey('Tour',on_delete=models.CASCADE)
    id_cyclist = models.ForeignKey('Cyclist',on_delete=models.CASCADE)
    point = models.IntegerField(default=0)
    details = models.CharField(max_length=20,default=None)
    def __str__(self):
        return(str(self.id_tour)+' /' + str(self.id_cyclist))

class Bet(models.Model):
    id_user = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    id_cyclist = models.ForeignKey('Cyclist',on_delete=models.CASCADE)
    id_league = models.ForeignKey('League',on_delete=models.CASCADE)
    price = models.IntegerField()
    stage = models.IntegerField()
    creation_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return(str(self.id_league)+' /' + str(self.id_user) + ' /' + str(self.id_cyclist))
    def really_delete(self, request, queryset):
        for obj in queryset:
            obj.delete()

class BetForm(forms.ModelForm):
   class Meta:
     model = Bet
     fields = ['price']

class Cyclist(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    Team = models.CharField(max_length=50)
    age = models.IntegerField()
    salary = models.IntegerField(default=100000)
    def __str__(self):
        return self.name
