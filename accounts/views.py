

# rest_framework
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.status import *


# Models
from django.contrib.auth.models import User


# Serializers
from .serializer import RegisterSerializer,LoginSerializer




class Login(APIView):


    def post(sefl,request:Request) -> (Response):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'status':'error',
                'error':serializer.errors
            },status=HTTP_400_BAD_REQUEST)

        
        result = serializer.login(data=serializer.data,model=User)
        
        if not result:
             return Response({
                'status':'error',
                'error':'Fail autentication'
            },status=HTTP_400_BAD_REQUEST)
           

        return Response({
            'status':'ok',
            'data':result
        },status=HTTP_200_OK)



class Register(APIView):


    def post(sefl,request:Request) -> (Response):
        serializer = RegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'status':'error',
                'error':serializer.errors
            },status=HTTP_400_BAD_REQUEST)

        result = serializer.register(model=User,data=serializer.data)

        if not result:
            return Response({
                'status':'error',
                'error':'Email exists'
            },status=HTTP_400_BAD_REQUEST)


        return Response({
            'status':'ok',
            'data':result
        },status=HTTP_200_OK)



"""


{
    "username":"asda",
    "email":"dsds@dasd.com",
    "password":"dsad"
}


{
   "email":"sdas@gmail.com",
   "password":"sadas"
}


"""




