from errno import ECANCELED

from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from ..models import WatchList, StreamPlatform, Review
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly, IsReviewUserOrReadOnly
from .pagination import WatchListPagination, UserReviewListPagination


class ReviewCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)
        
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)
        if len(review_queryset) > 0:
            raise ValidationError('Already a review exists!')
        
        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']
        else:
            watchlist.avg_rating = (serializer.validated_data['rating'] + watchlist.avg_rating) / 2
        
        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save(update_fields=['avg_rating', 'number_rating'])
        
        serializer.save(watchlist=watchlist, review_user=review_user)


class ReviewList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
    
class UserReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    pagination_class = UserReviewListPagination
    
    def get_queryset(self):
        # username = self.kwargs['username']
        username = self.request.query_params.get('username')
        return Review.objects.filter(review_user__username=username)
    
    
class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsReviewUserOrReadOnly]
    
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
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = WatchListPagination
    
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
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailsAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
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
            return Response({'result': 'Item deleted successfully'}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
        

class StreamPlatformAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
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
            return Response({'Error': serializer.errors}, status.HTTP_400_BAD_REQUEST)
        
        
class StreamPlatformDetailsAV(APIView):
    permission_classes = [IsAdminOrReadOnly]
    
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