from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at last christmas.")


def detail(request, list_id):
    return HttpResponse("You're looking at lists %s" % list_id)

def results(request, list_id):
    response = "You're looking at the results of list %s."
    return HttpResponse(response % list_id)

def vote(request, list_id):
    return HttpResponse("You're voting on question %s." % list_id)