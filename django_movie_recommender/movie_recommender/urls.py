from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_recommender, name='movie_recommender'),
    path('movies/search/', views.movie_search, name='movie_search'),
    path('movies/<int:id>/<int:page>', views.movie_details, name='movie_details'),
]