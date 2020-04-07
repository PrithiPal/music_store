from django.db import models

# Create your models here.
class Game(models.Model) : 
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='')
    about = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)
    publisher = models.CharField(max_length=100,blank=True)

    def __str__(self) : 
        return "{} by {}".format(self.name,self.publisher)
