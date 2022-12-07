from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', views.WatchDetailsAV.as_view(), name='movie-details'),
    path('stream/', views.StreamPlatformAV.as_view(), name='stream'),
    path('stream/<int:pk>/', views.StreamPlatformDetailsAV.as_view(), name='stream-details'),
    
    path('stream/<int:pk>/review-create/', views.ReviewCreate.as_view(), name='review-create'),
    path('stream/<int:pk>/reviews/', views.ReviewList.as_view(), name='review-list'),
    path('stream/review/<int:pk>/', views.ReviewDetails.as_view(), name='review-details'), 
    
    path('reviews/<str:username>', views.UserReviewList.as_view(), name='user-review-list'),
]
