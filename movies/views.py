from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie

def movies(request):
  movies = Movie.objects.all()
  context = {'movies': movies}
  return render(request, 'movies/movies.html', context)

def home(request):
  return render

def detail(request, id):
  movie = Movie.objects.get(pk=id)
  context = {'movie': movie}
  return render(request, 'movies/detail.html', context)

def add(request):
  title = request.POST.get('title')
  year = request.POST.get('year')

  if title and year:
    movie = Movie(title=title, year=year)
    movie.save()
    return HttpResponseRedirect('/movies')

  return render(request, 'movies/add.html')

def delete(request, id):
  try:
    movie = Movie.objects.get(pk=id)
  except:
    raise Http404('Movie does not exist.')
  movie.delete()
  return HttpResponseRedirect('/movies')