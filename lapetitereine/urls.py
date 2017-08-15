"""lapetitereine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from game.views import *

urlpatterns = [
    url(r'^game/',include('game.urls')),
    url(r'^registration/login/$',auth_views.login, name='login'),
    url(r'^registration/logout/$',logout_view, name='logout'),
    url(r'^game/league/(?P<league_id>[0-9]+)/$', show_league, name='league_view'),
    url(r'^game/new_league/$', show_new_league, name='new_league_view'),
    url(r'^game/subscribe_league/$', subscribe_league, name='subscribe_league_view'),
    url(r'^game/league/(?P<league_id>[0-9]+)/(?P<cyclist_id>[0-9]+)/$', show_bet, name='bet'),
    url(r'^game/league/(?P<league_id>[0-9]+)/cancel_offer/(?P<cyclist_id>[0-9]+)/$', cancel_offer, name='cancel_offer'),
    url(r'^game/league/(?P<league_id>[0-9]+)/regle/$', show_regle, name='regle'),
    url(r'^game/league/(?P<league_id>[0-9]+)/passage_round/$', show_passage_round, name='passage_round'),
    url(r'^game/league/(?P<league_id>[0-9]+)/my_cyclist/$', show_my_cyclist, name='my_cyclist'),
    url(r'^game/league/(?P<league_id>[0-9]+)/ranking/$', show_ranking, name='ranking'),
    url(r'^admin/',admin.site.urls),
]
