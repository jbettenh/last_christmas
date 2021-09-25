from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from .models import MovieList, Movie


def index(request):
    users = MovieList.objects.all()
    context = {'movie_lists': users}
    return render(request, 'christmasflix/index.html', context)


def detail(request, movielist_id):
    # view list of choices
    """
    movie_list = get_object_or_404(MovieList, pk=movielist_id)
    return render(request, 'christmasflix/detail.html', {'Lists': movie_list})
    return HttpResponse("You're looking at the list for %s." % view_lists)
    """
    #view_movies = get_object_or_404(MovieList, pk=movielist_id)
    view_movies = Movie.objects.get(id=movielist_id)
    template = loader.get_template('christmasflix/detail.html')
    context = {
        'latest_question_list': view_movies,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'christmasflix/detail.html', {'Lists': view_movies})




def results(request, movielist_id):
    #view_movies = get_object_or_404(MovieList, pk=movielist_id)
    view_movies = MovieList.objects.get(id=movielist_id)
    return render(request, 'christmasflix/results.html', {'movies': view_movies})
