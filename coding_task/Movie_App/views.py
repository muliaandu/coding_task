from django.shortcuts import render, redirect
from .models import Movie  # Import your Movie model
import requests

def listing(request):
    # Fetch all movies from the database
    movies = Movie.objects.all()
    return render(request, 'listing.html', {'movies': movies})
# def listing(request):
#     # URL of the JSON file
#     # json_url = 'https://drive.google.com/uc?id=18HZ_bqk-oMIUdU8HIP07KX86AEVV0KY0'

#     # # Fetch JSON data from the URL
#     # response = requests.get(json_url)
#     # if response.status_code == 200:
#     #     movies_data = response.json()
#     # else:
#     #     movies_data = []  # Set default value if unable to fetch data

#     # Pass the data to the template
#     return render(request, 'listing.html', {'movies': movies_data})

def detail(request, movie_id):
    # Fetch the movie with the given movie_id from the database
    movie = Movie.objects.get(pk=movie_id)
    return render(request, 'detail.html', {'movie': movie})

def search_results(request):
    query = request.GET.get('query')
    if query:
        # Filter movies based on the search query
        movies = Movie.objects.filter(name__icontains=query)
    else:
        movies = Movie.objects.all()

    return render(request, 'search_results.html', {'movies': movies, 'query': query})
