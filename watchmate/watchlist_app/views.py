# from django.shortcuts import render
# from django.http import JsonResponse

# from .models import Movie

# # Create your views here.
# def movie_list(request):
#     movies = Movie.objects.all()
#     data = {
#         'movies': list(movies.values())
#     }
#     print(data)
    
#     return JsonResponse(data, safe=False)


# def movie_details(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     data = {
#         'name': movie.name,
#         'description': movie.description,
#         'active': movie.active,
#     }
#     print(data)
    
#     return JsonResponse(data, safe=False)
