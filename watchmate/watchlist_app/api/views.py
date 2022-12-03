from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics

from ..models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer


class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    

class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

 
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request,  *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request,  *args, **kwargs)


# class ReviewDetails(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request,  *args, **kwargs)
    
#     # def put(self, request, *args, **kwargs):
#     #     return self.modify(request,  *args, **kwargs)
    

class WatchListAV(APIView):
    def get(self, request):
        try:
            movies = WatchList.objects.all()
            serializer = WatchListSerializer(movies, many=True) # add "context={'request': request}" into the argument-list for HyperlinkedRelatedField
            print(f"serializer.data = {serializer.data}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class WatchDetailsAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie) # add "context={'request': request}" into the argument-list for HyperlinkedRelatedField
            print(f"serializer.data = {serializer.data}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        watch_list = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(watch_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            movie.delete()
            return Response({'result': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        

class StreamPlatformAV(APIView):
    def get(self, request):
        try:
            platforms = StreamPlatform.objects.all()
            serializer = StreamPlatformSerializer(platforms, many=True) # add "context={'request': request}" into the argument-list for HyperlinkedRelatedField
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Error': 'Not found'}, status.HTTP_404_NOT_FOUND)
        
        
class StreamPlatformDetailsAV(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(platform) # add "context={'request': request}" into the argument-list for HyperlinkedRelatedField
            print(f"serializer.data = {serializer.data}")
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        stream_platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(stream_platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        try:
            stream_platform = StreamPlatform.objects.get(pk=pk)
            stream_platform.delete()
            return Response({'result': 'Item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
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