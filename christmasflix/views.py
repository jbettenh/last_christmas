from django.shortcuts import get_object_or_404, redirect, render

from .models import MovieList, Movie


def index(request):
    users = MovieList.objects.all()
    context = {'movie_lists': users}
    return render(request, 'christmasflix/index.html', context)


def detail(request, movielist_id):
    view_movies = get_object_or_404(MovieList, pk=movielist_id)
    return render(request, 'christmasflix/detail.html', {'movies': view_movies})


def results(request):
    view_movies = Movie.objects.all()
    return render(request, 'christmasflix/results.html', {'movies': view_movies})


def add_movie(request, movielist_id):
    current_list = MovieList.objects.get(id=movielist_id)
    Movie.objects.create(title=request.POST['movie_title'], movielist=current_list)
    return redirect(f'/christmasflix/{current_list.id}')
