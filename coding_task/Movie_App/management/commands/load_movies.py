import requests
from django.core.management.base import BaseCommand
from Movie_App.models import Movie

class Command(BaseCommand):
    help = 'Load movies from JSON file'

    def handle(self, *args, **kwargs):
        url = 'https://drive.google.com/uc?id=18HZ_bqk-oMIUdU8HIP07KX86AEVV0KY0'  # URL of the JSON file
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for non-200 status codes
            movies_data = response.json()
            for movie_data in movies_data:
                Movie.objects.create(
                    name=movie_data['name'],
                    description=movie_data['description'],
                    imgPath=movie_data['imgPath'],
                    duration=movie_data['duration'],
                    genre=movie_data['genre'],
                    language=movie_data['language'],
                    type=movie_data['mpaaRating']['type'],
                    label=movie_data['mpaaRating']['label'],
                    userRating=movie_data['userRating']
                )
            self.stdout.write(self.style.SUCCESS('Successfully loaded movies data'))
        except requests.RequestException as e:
            self.stderr.write(self.style.ERROR(f'Failed to download movies data: {e}'))
