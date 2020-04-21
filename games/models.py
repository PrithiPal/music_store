from django.db import models

# Create your models here.
class Game(models.Model) : 
    
    name = models.CharField(max_length=20)
    summary = models.CharField(max_length=1000)
    ratings = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100,blank=True)
    popularity = models.DecimalField(max_digits=500000,decimal_places=4,default=0.0)
    igdb_url = models.URLField(default="https://www.igdb.com/games")

    ## access cover using related_name ; game_cover_id    

    def __str__(self) : 

        return "{} by {}".format(self.name,self.publisher)


class Cover(models.Model) : 
    id = models.IntegerField(primary_key=True)
    alpha_channel = models.BooleanField(default=False)
    animated = models.BooleanField(default=False)
    game = models.ForeignKey(Game,on_delete=models.CASCADE,related_name="game_cover_id")
    height = models.IntegerField()
    image_id = models.CharField(max_length=100)
    url = models.URLField()
    width = models.IntegerField()



class Size(models.Model) : 
    title = models.CharField(max_length=100)

    def __str__(self) : 
        return self.title 

class Pizza(models.Model) : 
    toppings1 = models.CharField(max_length=100)
    toppings2 = models.CharField(max_length=100)

    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    

