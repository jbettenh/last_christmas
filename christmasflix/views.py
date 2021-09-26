from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import generic

from .models import MovieList, Movie


class IndexView(generic.ListView):
    template_name = 'christmasflix/index.html'
    context_object_name = 'movie_lists'

    def get_queryset(self):
        return MovieList.objects.all()


class DetailView(generic.DetailView):
    model = MovieList
    context_object_name = 'movies'
    template_name = 'christmasflix/detail.html'


def results(request):
    view_movies = Movie.objects.all()
    return render(request, 'christmasflix/results.html', {'movies': view_movies})


def add_movie(request, movielist_id):
    current_list = MovieList.objects.get(id=movielist_id)
    Movie.objects.create(title=request.POST['movie_title'], movielist=current_list)
    return redirect(reverse('christmasflix:detail', args=(current_list.id,)))
