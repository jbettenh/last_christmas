from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView

from .models import MovieList, Movie

from .omdbmovies import search_movie, get_movie_info


class IndexView(ListView):
    context_object_name = 'movie_lists'
    template_name = 'christmasflix/index.html'

    def get_queryset(self):
        return MovieList.objects.all()


def add_list(request):
    new_list = MovieList.objects.create(name=request.POST['movie_title'])
    return redirect(reverse('christmasflix:movie_list', args=(new_list.id,)))


def delete_list(request, list_id):
    current_list = MovieList.objects.get(id=list_id)
    current_list.delete()
    return redirect(reverse('christmasflix:index'))


def add_movie(request, movielist_id, movie_title):
    current_list = MovieList.objects.get(id=movielist_id)
    movie_info = get_movie_info(movie_title)
    Movie.objects.create(title=movie_info['Title'],
                         year=movie_info['Year'],
                         img_url=movie_info['Poster'],
                         movielist=current_list)

    return redirect(reverse('christmasflix:movie_list', args=(current_list.id,)))


def delete_movie(request, movielist_id, movie_id):
    current_movie = Movie.objects.get(id=movie_id)
    current_movie.delete()
    return redirect(reverse('christmasflix:movie_list', args=(movielist_id,)))


class ResultsView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'christmasflix/results.html'

    def get_queryset(self):
        search = search_movie(self.request.GET.get('movie_title'))
        return search['Search']


class MovieListView(ListView):
    model = MovieList
    context_object_name = 'movies'
    template_name = 'christmasflix/movie_list.html'


class MoviesView(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'christmasflix/movies.html'



