from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import MovieList, Movie


def index(request):
    users = MovieList.objects.all()
    context = {'movie_lists': users}
    return render(request, 'christmasflix/index.html', context)


def detail(request, movielist_id):
    #view_movies = get_object_or_404(MovieList, pk=movielist_id)
    view_movies = MovieList.objects.get(id=movielist_id)
    return render(request, 'christmasflix/detail.html', {'movies': view_movies})


def results(request, movielist_id):
    #view_movies = get_object_or_404(MovieList, pk=movielist_id)
    view_movies = MovieList.objects.get(id=movielist_id)
    return render(request, 'christmasflix/results.html', {'movies': view_movies})
