from django.http import HttpResponse
from django.shortcuts import render

from .models import MovieList


def index(request):
    latest_movie_list = MovieList.objects.order_by('id')[:5]
    context = {'movie list': latest_movie_list}
    return render(request, 'christmasflix/index.html', context)


def detail(request, movies_id):
    return HttpResponse("You're looking at lists %s" % movies_id)


def results(request, movies_id):
    response = "You're looking at the results of list %s."
    return HttpResponse(response % movies_id)


def vote(request, movies_id):
    return HttpResponse("You're voting on question %s." % movies_id)