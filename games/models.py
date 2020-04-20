from django.db import models

# Create your models here.
class Game(models.Model) : 
    
    name = models.CharField(max_length=20)
    cover = models.ImageField(upload_to='')
    summary = models.CharField(max_length=1000)
    ratings = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100,blank=True)
    popularity = models.DecimalField(max_digits=500000,decimal_places=4,default=0.0)
    igdb_url = models.URLField(default="https://www.igdb.com/games")

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
    

