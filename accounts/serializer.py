# rest_framework
from rest_framework import serializers


# Models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# Django
from django.contrib.auth.hashers import check_password,make_password




class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


    def login(self,data:dict,model:User) -> (dict):
        try:
            user = model.objects.get(email=data['email'])
            if check_password(data['password'],user.password):
                token = Token.objects.get_or_create(user=user)
                return({ 'token':token[0].key })


        except Exception as e:
            pass



class RegisterSerializer(serializers.Serializer):
    
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    

    def register(self,data:dict,model:User) -> (dict):
        try:
            user = model.objects.create_user(**data)
            token = Token.objects.create(user=user)
            return ({ 'token':token.key })
        except Exception as e:
            return None