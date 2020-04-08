from django.shortcuts import render, get_object_or_404
from .models import Game 

def home(request) : 
    games = Game.objects.all()[:3]
    return render(request,'games/home.html',{'games':games})

def detail(request,game_id) : 
    game = get_object_or_404(Game,pk=game_id)
    return render(request,'games/detail.html',{'game':game})

def order(request) : 
    return render(request,'games/order.html')