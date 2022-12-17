

# rest_framework
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


# models
from .models import Movie,MovieView


# Serializers
from .serializer import *


class RandomItem(APIView):

	""" Obtiene un item aleatorio """
    
	def get(self,request:Request) -> (Response):
		mode_object = RandomItemSerializer().get_random_move(
			model=Movie
		)
		return Response({
			'status':'ok',
			'data':mode_object
			},
		status=HTTP_200_OK)



class Items(ListCreateAPIView):

	""" Se encarga de mostrar un listado de los datos """

	serializer_class = ItemsSerializer
	permission_classes = [ IsAuthenticated ]
	authentication_classes = [ TokenAuthentication ]

	def list(self, request, *args, **kwargs) -> (Response):
		queryset = self.get_queryset()
		serializer = ItemsSerializer(queryset, many=True)
		return Response({ 'data':serializer.data })
		

	def get_queryset(self):
		if self.request.GET.get('order_by'):
			""" Organiza los datos degun la query indicada """
			order_by = self.request.GET['order_by']

			if order_by == 'name':
				return Movie.objects.all().order_by(f'{order_by}')

			if order_by == 'rate':
				result = Movie.objects.all()
				return sorted(result,key=lambda t: t.rate,reverse=True)
			
			return Movie.objects.all().order_by(f'-{order_by}')

		if self.request.GET.get('q'):
			""" Encarga de buscar por una query """

			q = self.request.GET['q']
			return Movie.objects.filter(name__contains=q)


		return Movie.objects.all()



class ItemsViews(APIView):

	permission_classes = [ IsAuthenticated ]
	authentication_classes = [ TokenAuthentication ]


	def get(self,request) -> (Response):

		""" Retorna una lista de items marcados como vistos """

		retults = ItemsViewsSerializer().get_views_list(
			user=request.user,
			viewModel=MovieView
		)

		return Response({
			'status':'ok',
			'data':retults
		})



class Item(APIView):

	permission_classes = [IsAuthenticated]
	authentication_classes = [ TokenAuthentication ]


	def get(self,request:Request,id:int) -> (Response):

		""" Permite obtiener los datos de un item apraves de su id """

		result = ItemSerializer().get_data(
			id=id,
			model=Movie,
			user=request.user,
			rateModel=MovieRating
		)

		if not result:
			return Response({
				'status':'error',
				'data':'Item not exists'
			},status=HTTP_400_BAD_REQUEST)


		return Response({
			'status':'ok',
			'data':result
		},status=HTTP_200_OK)


class ItemViews(APIView):

	permission_classes = [IsAuthenticated]
	authentication_classes = [ TokenAuthentication ]


	def post(self,request:Request,id:int) -> (Response):

		""" Permite registrar una visualizacion a un item """

		result = MovieViewSerializer().set_view(
			user=request.user,
			viewModel=MovieView,
			model=Movie,id=id
		)

		if not result:
			return Response({
				'status':'error',
				'messege':'Error to set the view'
			},status=HTTP_400_BAD_REQUEST)
		

		return Response({
			'status':'ok',
			'messege':'View created'
		},status=HTTP_200_OK)


class RatingItem(APIView):

	permission_classes = [ IsAuthenticated ]
	authentication_classes = [ TokenAuthentication ]

	def post(self,request:Request,id:int) -> (Response):

		""" Permite añadir puntuacion a un item """

		serializer = RatingSerializer(data=request.data)

		if not serializer.is_valid():
			return Response({
				'status':'error',
				'messege':serializer.errors
			},status=HTTP_400_BAD_REQUEST)

		result = serializer.set_rate(
			id=id,
			data=serializer.data,
			model=Movie,
			user=request.user,
			rateModel=MovieRating
		)

		if not result:
			return Response({
				'status':'error',
				'messege':'Fail to add rate'
			},status=HTTP_400_BAD_REQUEST)	
		
		return Response({ 'status':'ok', },status=HTTP_200_OK)






