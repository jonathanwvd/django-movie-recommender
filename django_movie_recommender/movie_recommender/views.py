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

def request_recommendations(movie_id, page):
  request_url = f'{api_base_url}/movie/{movie_id}/recommendations?api_key={API_KEY}&page={page}'
  res = requests.get(request_url)
  return res.json()['results']

def request_top_rated():
  request_url = f'{api_base_url}/movie/top_rated?api_key={API_KEY}'
  res = requests.get(request_url)
  return res.json()['results']

def request_search(searched):
  request_url = f'{api_base_url}/search/movie?api_key={API_KEY}&language=en-US&query={searched}&page=1&include_adult=false'
  res = requests.get(request_url)
  return res.json()['results']

def get_recommendation_context(id, page, movie_info):
  recommendations = request_recommendations(id, page)
  top_rated = [] 
  if len(recommendations) == 0:
    top_rated = request_top_rated()

  context = {
    'similar_movies': recommendations,
    'movie_selected': movie_info,
    'next_page': page + 1,
    'top_rated': top_rated
  }

  return context

# Views

def movie_recommender(request):
  template = loader.get_template('pages/index.html')
  context = {'top_rated': request_top_rated()
  }
  return HttpResponse(template.render(context, request))


def movie_details(request, id, page):
  movie_info = request_movie_info(id)
  template = loader.get_template('pages/movie_details.html')

  context = get_recommendation_context(id, page, movie_info)
  return HttpResponse(template.render(context, request))


def movie_search(request):
  if request.method == 'POST':
    searched = request.POST['searched']
    movie_info = request_search(searched)

    if len(movie_info) > 0:
      template = loader.get_template('pages/movie_details.html')

      context = get_recommendation_context(id=movie_info[0]['id'], page=1, movie_info=movie_info[0])
      return HttpResponse(template.render(context, request))

    else:
      template = loader.get_template('pages/movie_not_found.html')
      context = {'top_rated': request_top_rated()}
      return HttpResponse(template.render(context, request))
