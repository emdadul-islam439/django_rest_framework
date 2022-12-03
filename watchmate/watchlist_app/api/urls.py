from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailsAV.as_view(), name='movie-details'),
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', views.StreamPlatformDetailsAV.as_view(), name='stream-details'),
    
    path('reviews', views.ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetails.as_view(), name='review-details'), 
]
