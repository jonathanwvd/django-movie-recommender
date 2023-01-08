from django.http import HttpResponse
from django.template import loader

import requests
import os

# load TMDB API Key
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
API_KEY = os.environ['API_KEY']


api_base_url = 'https://api.themoviedb.org/3'

def request_movie_info(movie_id):
  request_url = f'{api_base_url}/movie/{movie_id}?api_key={API_KEY}'
  res = requests.get(request_url)
  return res.json()

def request_recommendations(movie_id):
  request_url = f'{api_base_url}/movie/{movie_id}/recommendations?api_key={API_KEY}'
  res = requests.get(request_url)
  return res.json()['results']

def request_top_rated():
  request_url = f'{api_base_url}/movie/top_rated?api_key={API_KEY}'
  res = requests.get(request_url)
  return res.json()['results']


def movie_recommender(request):
  """"""
  template = loader.get_template('pages/index.html')
  context = {'top_rated': request_top_rated()
  }

  return HttpResponse(template.render(context, request))

def movie_details(request, id):
  movie_info = request_movie_info(id)
  template = loader.get_template('pages/movie_details.html')

  context = {
    'similar_movies': request_recommendations(id),
    'movie_info': movie_info,
  }


  return HttpResponse(template.render(context, request))