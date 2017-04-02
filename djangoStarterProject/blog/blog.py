from django.http import HttpResponse


def index(request):
    return HttpResponse("Index page.")

def about(request):
    return HttpResponse("About page.")