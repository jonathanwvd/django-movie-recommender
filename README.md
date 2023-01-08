# Django Movie Recommendation

This simple Django application suggests new movies based on a selected one.

The application uses the [The Movie DB API](https://developers.themoviedb.org/3) to get information about movies as well as covers and images.

"The Movie DB" recommendations are used, although some recommendation algorithm could be easily integrated into this application.

This [Netflix-based bootstrap template](https://w3hubs.com/netflix-home-page-in-bootstrap-5/) was used.


Demo: https://my-next-movie.herokuapp.com/

## Get a TMDB API Key
You will need a TMDB API Key to allow the application to request TMDB data. To do this, follow [these steps](https://developers.themoviedb.org/3/getting-started/introduction).

Afterwards, create a file called `.env` in the root folder and paste:

`API_KEY = 'your_api_key'`

## Setup the project

Clone this repository to your local machine. Inside the root directory, run the following command (Linux or Mac):

`python3 -m venv venv`

Activate your virtual environment:

`source venv/bin/activate`

Run the following command in the root directory to install the requirements:

`pip install -r requirements.txt`

Navigate to the django_movie_recommender folder:

`cd ../django_movie_recommender`

Run:

`python manage.py runserver`

Open your browser and go to this address:

`http://127.0.0.1:8000`