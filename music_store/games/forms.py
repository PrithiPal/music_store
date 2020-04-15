from django import forms 
from .models import Pizza,Size

class PizzaForm(forms.ModelForm) : 
    

    size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)

    #image = forms.ImageField()
    
    class Meta:
        model = Pizza 
        fields = ['toppings1','toppings2','size']
        labels = {'toppings1':'Topping 1','toppings2':'Topping 2'}

        

#class PizzaForm(forms.Form) : 
#    CHOICES=[('pep','pepperoni'),('cheese','Cheese'),('Olives','olives')]
#    toppings = forms.MultipleChoiceField(choices=CHOICES,widget=forms.CheckboxSelectMultiple)
