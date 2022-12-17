

# Django
from django.db import models


# Models
from django.contrib.auth.models import User


# libs
import math


class Movie(models.Model):


    preview = models.ImageField(upload_to='media')

    name = models.CharField(
        max_length=1000,
        default=None,
        null=None,
        help_text='Name of the move'
    )
    
    gender = models.CharField(
        max_length=1000,
        default=None,
        null=None,
        help_text='Gender of the move'
    )

    isMove = models.BooleanField(default=True)

    views = models.IntegerField(
        default=None,
        null=None,
        help_text='Number of the views'
    )

    score = models.IntegerField(
        default=None,
        null=None,
        help_text='Name of the score'
    )


    @property
    def item_type(self):
        return 'Pelicula' if self.isMove else 'Serie'

    
    @property
    def vews(self):
        views = MovieView.objects.filter(movieItem=self)
        return len(views)

    
    @property
    def rate(self):
        rating_list = MovieRating.objects.filter(movieItem=self).values('score')
        prom_score = 0
        for rate in rating_list:
            prom_score += rate['score']

        return round(prom_score/len(rating_list),1) if len(rating_list) > 0 else 0
    

    def __str__(self) -> (str):
        return self.name






class MovieView(models.Model):

    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    movieItem = models.ForeignKey(to=Movie,on_delete=models.CASCADE)



class MovieRating(models.Model):

    user = models.ForeignKey(to=User,on_delete=models.CASCADE)
    movieItem = models.ForeignKey(to=Movie,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


