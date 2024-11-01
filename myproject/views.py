from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hello world I'm DJango")

def aboutpage(request):
    return HttpResponse("Hello world I'm DJango about")