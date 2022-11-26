from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

from ..models import Movie
from .serializers import MovieSerializer


class MovieListAV(APIView):
    def get(self, request):
        try:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            print(f"serializer.data = {serializer.data}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'Error': 'Movie list not found'}, status.HTTP_404_NOT_FOUND)
        
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class MovieDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie)
            print(f"serializer.data = {serializer.data}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response({'result': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
    
        

# Create your views here.
# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         try:
#             movies = Movie.objects.all()
#             serializer = MovieSerializer(movies, many=True)
#             print(f"serializer.data = {serializer.data}")
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except:
#             return Response({'Error': 'Movie list not found'}, status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#             serializer = MovieSerializer(movie)
#             print(f"serializer.data = {serializer.data}")
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         except:
#             return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     if request.method == 'DELETE':
#         try:
#             movie = Movie.objects.get(pk=pk)
#             movie.delete()
#             return Response({'result': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
#         except:
#             return Response(status=status.HTTP_400_BAD_REQUEST)