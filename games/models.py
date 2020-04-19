from django.db import models

# Create your models here.
class Game(models.Model) : 
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='')
    about = models.CharField(max_length=1000)
    rating = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100,blank=True)

    def __str__(self) : 
        return "{} by {}".format(self.name,self.publisher)


class Size(models.Model) : 
    title = models.CharField(max_length=100)

    def __str__(self) : 
        return self.title 

class Pizza(models.Model) : 
    toppings1 = models.CharField(max_length=100)
    toppings2 = models.CharField(max_length=100)

    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    
