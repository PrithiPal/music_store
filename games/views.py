from django.shortcuts import render, get_object_or_404
from .models import Game, Pizza 
from .forms import PizzaForm
from django.forms import formset_factory

def home(request) : 
    games = Game.objects.all()[:3]
    return render(request,'games/home.html',{'games':games})

def detail(request,game_id) : 
    game = get_object_or_404(Game,pk=game_id)
    return render(request,'games/detail.html',{'game':game})

def inventory(request) : 
    games = Game.objects.all()
    return render(request,'games/inventory.html',{'games':games})

def order(request) : 
    if request.method=='POST' : 
        
        filled_form = PizzaForm(request.POST,request.FILES)

        if filled_form.is_valid() : 
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id 
            topping1 = filled_form.cleaned_data['toppings1']
            topping2 = filled_form.cleaned_data['toppings2']
            size = filled_form.cleaned_data['size']
            note = "Thanks. Order = {} with {} and {}".format(topping1,topping2,size)
            filled_form = PizzaForm()
        else:
            created_pizza_pk = None
            note = "Pizza is not created yet.."    
        return render(request,'games/order.html',{'pizzaform':filled_form,'note':note,'created_pizza_pk':created_pizza_pk})

    else:
        form = PizzaForm()
        return render(request,'games/order.html',{'pizzaform':form})

def experiment(request) : 
    game = Game.objects.all()[0]
    return render(request,'games/experiment.html',{'game':game});

def edit_order(request,pk):
    pizza = Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza)
    
    if request.method=='POST': 
        filled_form = PizzaForm(request.POST,instance=pizza)
        if filled_form.is_valid() : 
            filled_form.save()
            form = filled_form 
            note = 'order has been updated.'
            return render(request,'games/edit_order.html',{'note':note,'pizzaform':form,'pizza':pizza})

    return render(request,'games/edit_order.html',{'pizzaform':form,'pizza':pizza})


