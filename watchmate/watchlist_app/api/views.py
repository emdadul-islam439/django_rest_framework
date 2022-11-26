from rest_framework.response import Response
from rest_framework.decorators import api_view

from ..models import Movie
from .serializers import MovieSerializer

# Create your views here.
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    print(f"serializer.data = {serializer.data}")
    return Response(serializer.data)


@api_view(['GET'])
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    print(f"serializer.data = {serializer.data}")
    return Response(serializer.data)
