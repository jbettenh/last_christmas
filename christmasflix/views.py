from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import MovieList, Movie


def index(request):
    latest_movie_list = MovieList.objects.order_by('id')[:5]
    context = {'movie list': latest_movie_list}
    return render(request, 'christmasflix/index.html', context)


def detail(request, movielist_id):
    """
    movie_list = get_object_or_404(MovieList, pk=movielist_id)
    return render(request, 'christmasflix/detail.html', {'Lists': movie_list})
    """
    view_lists = get_object_or_404(MovieList, pk=movielist_id)
    return HttpResponse("You're looking at the list for %s." % view_lists)


def results(request, movielist_id):
    #view_movies = get_object_or_404(MovieList, pk=movielist_id)
    view_movies = MovieList.objects.get(id=movielist_id)
    return render(request, 'christmasflix/results.html', {'movies': view_movies})
