from django.shortcuts import render
from django.http import HttpResponse
from game.models import *
from game.function import *
from django.contrib.auth.models import User
from django.template import loader
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.views import logout
from django.shortcuts import redirect
from django.core.exceptions import ValidationError

def logout_view(request):
    logout(request)
    return redirect('/registration/login/')

def show_regle(request,league_id):
    template = loader.get_template('lapetitereine/regles.html')
    league = League.objects.get(id = league_id)
    context = {
        'league':league,
    }
    return HttpResponse(template.render(context, request))

def show_new_league(request):
    user = request.user
    league = League(id_creator_id=user.id,)
    league_form= LeagueForm(request.POST or None)
    if request.method == 'POST':
        league_form= LeagueForm(request.POST, instance = league)
        if league_form.is_valid():
            league_form.save(commit=False)
            league.id_tour_id = 1
            league.save()
            n_id = league.id
            link = Link_user_league()
            link.id_user_id =user.id
            link.id_league_id = league.id
            link.save()
            return HttpResponseRedirect(reverse('index'))
    # if a GET (or any other method) we'll create a blank form
    else:
        league_form = LeagueForm()
    context = {
    'user': user,
    'league_form': league_form,
    }
    return render(request, 'lapetitereine/new_league.html', context)


def index(request):
    username = None
    if request.user.is_authenticated():
        username = request.user.username
        user_id = request.user.id
        list_of_league = Link_user_league.objects.filter(id_user_id = user_id)
        for ro in list_of_league:
            el = League.objects.get(id = ro.id_league_id)
            ro.name = el.name
        template = loader.get_template('lapetitereine/index.html')
        context = {
            'username':username,
            'list_of_league': list_of_league,
        }
        return(HttpResponse(template.render(context, request)))
    else:
        return redirect('login')

# Return the content of a specific league
def show_league(request,league_id):
    user_id = request.user.id
    user = request.user
    league = League.objects.get(id = league_id)
    list_of_cyc = Cyclist.objects.all()
    list_of_bet = Bet.objects.filter(id_user = user_id,id_league = league_id, stage = league.step)
    #Getting the remaining amount of
    money = calculate_money(user_id,league_id,league.step)
    if  league.step == 0:
        list_of_player = Link_user_league.objects.filter(id_league = league_id)
        for player in list_of_player:
            el = User.objects.get(id = player.id_user_id)
            player.name = el.username
        template = loader.get_template('lapetitereine/league_round0.html')
        context = {
            'user': user,
            'league':league,
            'list_of_player':list_of_player,
        }
        return HttpResponse(template.render(context, request))
    if  league.step == 1:
        list_of_cyclist = find_cyclist_excluding_bought(list_of_cyc,list_of_bet)
        template = loader.get_template('lapetitereine/league_round1.html')
        for bet in list_of_bet:
            el = Cyclist.objects.get(id = bet.id_cyclist_id)
            bet.name = el.name
        context = {
            'user': user,
            'league':league,
            'list_of_cyclist':list_of_cyclist,
            'list_of_bet': list_of_bet,
            'money': money,
        }
        return HttpResponse(template.render(context, request))
    elif league.step == 2:
        template = loader.get_template('lapetitereine/league_round1.html')
        list_of_bought = Link_user_league_cyclist.objects.filter(id_league_id=league_id)
        list_of_cyclist1 = find_cyclist_excluding_bought(list_of_cyc,list_of_bought)
        list_of_cyclist = find_cyclist_excluding_bought(list_of_cyclist1,list_of_bet)
        for bet in list_of_bet:
            el = Cyclist.objects.get(id = bet.id_cyclist_id)
            bet.name = el.name
        context = {
            'user': user,
            'league':league,
            'list_of_cyclist':list_of_cyclist,
            'list_of_bet': list_of_bet,
            'money': money,
        }
        return HttpResponse(template.render(context, request))
    elif league.step == 3:
        template = loader.get_template('lapetitereine/league_round1.html')
        list_of_bought = Link_user_league_cyclist.objects.filter(id_league_id=league_id)
        list_of_cyclist1 = find_cyclist_excluding_bought(list_of_cyc,list_of_bought)
        list_of_cyclist = find_cyclist_excluding_bought(list_of_cyclist1,list_of_bet)
        for bet in list_of_bet:
            el = Cyclist.objects.get(id = bet.id_cyclist_id)
            bet.name = el.name
        context = {
            'user': user,
            'league':league,
            'list_of_cyclist':list_of_cyclist,
            'list_of_bet': list_of_bet,
            'money': money,
        }
        return HttpResponse(template.render(context, request))
    elif league.step == 4:
        return redirect('my_cyclist',league_id)

def show_bet(request,league_id,cyclist_id):
    user_id = request.user.id
    link_user_league_id =Link_user_league.objects.get(id_user_id=user_id,id_league_id=league_id).id
    league = League.objects.get(id = league_id)
    stage = league.step
    money = calculate_money(user_id,league_id,league.step)
    bet = Bet(id_user_id=user_id,)
    bet_form= BetForm(request.POST or None)
    cyclist = Cyclist.objects.get(id=cyclist_id)
    list_of_bet = Bet.objects.filter(id_user = user_id,id_league = league_id, stage = league.step)
    if request.method == 'POST':
        if league.step == 1 or league.step == 2:
            bet_form= BetForm(request.POST, instance = bet)
            if bet_form.is_valid():
                if good_bet(link_user_league_id, bet_form.cleaned_data['price'],cyclist_id,user_id,league.id,stage):
                    bet_form.save(commit=False)
                    bet.id_user_id = request.user.id
                    bet.id_league_id = league.id
                    bet.id_cyclist_id = cyclist.id
                    bet.stage = league.step
                    bet.save()
                    return HttpResponseRedirect(reverse('league_view', args=(league_id,)))
        if league.step == 3:
            bet_form= BetForm(request.POST, instance = bet)
            if bet_form.is_valid():
                bet_form.save(commit=False)
                bet.id_user_id = request.user.id
                bet.id_league_id = league.id
                bet.id_cyclist_id = cyclist.id
                bet.stage = league.step
                bet.save()
                new_cyc = Link_user_league_cyclist()
                new_cyc.id_cyclist_id = bet.id_cyclist_id
                new_cyc.id_league_id = league_id
                new_cyc.id_user_id = bet.id_user_id
                new_cyc.save()
                return HttpResponseRedirect(reverse('league_view', args=(league_id,)))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = BetForm()
    context = {
    'cyclist': cyclist,
    'money': money,
    'league':league,
    'bet_form': bet_form,
    }
    return render(request, 'lapetitereine/bet.html', context)


def subscribe_league(request):
    user_id = request.user.id
    join_form= JoinForm(request.POST or None)
    if request.method == 'POST':
        join_form= JoinForm(request.POST)
        if join_form.is_valid():
            ref = League.objects.get(reference = join_form.cleaned_data['reference'])
            if type(ref) == League:
                link = Link_user_league()
                link.id_user_id = request.user.id
                link.id_league_id = ref.id
                link.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect(reverse('regle'))
    else:
        form = JoinForm()
    context = {
    'join_form':join_form,
    }
    return render(request, 'lapetitereine/subscribe_league.html', context)


def show_passage_round(request,league_id):
    league = League.objects.get(id = league_id)
    creator_id = request.user.id
    creator = request.user
    list_of_user = Link_user_league.objects.filter(id_league_id=league_id)
    list_of_bet = Bet.objects.filter(id_league_id=league_id,stage=league.step)
    list_of_cyclist = find_cyclist(list_of_bet)
    money_dict = {}
    if league.step == 1 or league.step == 2:
        money_dict = {}
        for cyclist_id in list_of_cyclist:
            list_of_try = Bet.objects.filter(id_league_id=league_id,stage=league.step,id_cyclist_id=cyclist_id)
            list_of_try = list_of_try.order_by('-price')
            best_bet = list_of_try[0]
            money_dict = add_dict(money_dict,best_bet.id_user_id,best_bet.price)
            new_cyc = Link_user_league_cyclist()
            new_cyc.id_cyclist_id = best_bet.id_cyclist_id
            new_cyc.id_league_id = league_id
            new_cyc.id_user_id = best_bet.id_user_id
            new_cyc.save()
        for user in money_dict:
            person = Link_user_league.objects.get(id_user_id=user,id_league_id=league_id)
            person.money = person.money - money_dict[user]
            person.save()
    if league.step == 3:
        league.step = 4
        league.save()
    if league.step == 2:
        league.step = 3
        league.save()
    if league.step == 1:
        league.step = 2
        league.save()
    if league.step == 0:
        league.step = 1
        league.save()
    context = {
    'league':league,
    'money_dict':money_dict,
    }
    return render(request, 'lapetitereine/passage_round.html', context)

def show_my_cyclist(request,league_id):
    league = League.objects.get(id = league_id)
    user_id = request.user.id
    user = request.user
    list_of_cyc = Link_user_league_cyclist.objects.filter(id_user_id=user_id,id_league_id=league_id)
    for cyclist in list_of_cyc:
        cyclist.point = calculate_point_cyc(cyclist.id_cyclist_id,league.id_tour_id)
        cyclist.save()
    list_of_cyclist = Link_user_league_cyclistTable(list_of_cyc)
    template = loader.get_template('lapetitereine/my_cyclist.html')
    context = {
        'user': user,
        'league':league,
        'list_of_cyclist':list_of_cyclist,
    }
    return HttpResponse(template.render(context, request))

def show_ranking(request,league_id):
    league = League.objects.get(id = league_id)
    user = request.user
    list_of_player = Link_user_league.objects.filter(id_league = league_id)
    for player in list_of_player:
        player.point = calculate_point(player.id_user_id,league_id,league.id_tour_id)
        player.name = User.objects.get(id=player.id_user_id).username
    template = loader.get_template('lapetitereine/ranking.html')
    context = {
        'user': user,
        'league':league,
        'list_of_player':list_of_player,
    }
    return HttpResponse(template.render(context, request))

def cancel_offer(request,league_id,cyclist_id):
    user_id = request.user.id
    league = League.objects.get(id = league_id)
    # The cyclist id is in reality the bet_id
    real_cyclist_id = Bet.objects.get(id=cyclist_id).id_cyclist_id
    bet = Bet.objects.filter(id_user = user_id,id_league = league_id,id_cyclist=real_cyclist_id, stage = league.step)
    bet.delete()
    template = loader.get_template('lapetitereine/cancel_offer.html')
    context = {
        'league':league,
        'cyclist_id':cyclist_id
    }
    return HttpResponse(template.render(context, request))
