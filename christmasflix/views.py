from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import MovieList, Movie


class IndexView(generic.ListView):
    context_object_name = 'movie_lists'
    template_name = 'christmasflix/index.html'

    def get_queryset(self):
        return MovieList.objects.all()


def add_list(request):
    new_list = MovieList.objects.create(name=request.POST['movie_title'])
    return redirect(reverse('christmasflix:detail', args=(new_list.id,)))


def add_movie(request, movielist_id):
    current_list = MovieList.objects.get(id=movielist_id)
    Movie.objects.create(title=request.POST['movie_title'], movielist=current_list)
    return redirect(reverse('christmasflix:detail', args=(current_list.id,)))


class DetailView(generic.DetailView):
    model = MovieList
    context_object_name = 'movies'
    template_name = 'christmasflix/detail.html'


class MoviesView(generic.ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'christmasflix/movies.html'



