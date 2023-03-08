from django.http import HttpResponse
from django.shortcuts import render

def movies(request):
  context = {
    'movies': [
      {
        'id': 8,
        'title': 'Jaws',
        'year': 1975
      },
      {
        'id': 2,
        'title': 'Cleopatra',
        'year': 1963
      },
      { 
        'id': 3,
        'title': 'La Cage aux Folles',
        'year': 1978
      },
      {
        'id': 4,
        'title': 'Moonstruck',
        'year': 1987
      }
    ]
  }
  return render(request, 'movies/movies.html', context)

def home(request):
  return render