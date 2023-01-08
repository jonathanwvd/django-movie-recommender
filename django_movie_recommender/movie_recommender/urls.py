from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_recommender, name='movie_recommender'),
    path('movies/details/<int:id>', views.movie_details, name='movie_details'),
]