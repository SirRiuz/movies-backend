


# rest_framework
from rest_framework import serializers


# libs
import random


# Models
from .models import *
from django.contrib.auth.models import User



class RandomItemSerializer(serializers.Serializer):

    def get_random_move(self,model:Movie) -> (object):
        return random.choice(model.objects.all().values())



class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [ 'id','name','gender','preview','item_type','views','rate' ]




class MovieViewSerializer(serializers.Serializer):
    
    def set_view(self,user:User,model:Movie,id:int,viewModel:MovieView) -> (bool):
        try:
            item = model.objects.get(id=id)
            viewModel.objects.create(user=user,movieItem=item)
            return True
        except Exception as e:
            pass



class ItemSerializer(serializers.Serializer):

    def get_data(self,id:int,model:Movie,rateModel:MovieRating,user:User) -> (dict):
        try:
            item = model.objects.get(id=id)
            rate = rateModel.objects.filter(
                movieItem=item,
                user=user
            ).values()
            return({
                **ItemsSerializer(item,many=False).data,
                'my-rate':rate[0] if rate else None
            })
        except:
            pass


class RatingSerializer(serializers.Serializer):

    score = serializers.IntegerField(required=True)


    def get_rate(self,**kwargs) -> (bool):
        print('Df')


    def set_rate(self,**kwargs) -> (bool):
        try:
            id = kwargs['id']
            score = kwargs['data']['score']
            item = kwargs['model'].objects.get(id=id)
            kwargs['rateModel'].objects.create(
                user=kwargs['user'],
                movieItem=item,
                score=score
            )
            
            return True
        except Exception as e:
            raise(e)





class ItemsViewsSerializer(serializers.Serializer):

    def get_views_list(self,user:User,viewModel:MovieView) -> (list):
        views = viewModel.objects.filter(user=user)
        viewlist = []

        for item in views:
            viewlist.append(ItemsSerializer(item.movieItem,many=False).data)
        return viewlist
