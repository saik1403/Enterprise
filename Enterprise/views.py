from django.http import HttpResponse
def HomePage(request):
    return HttpResponse("Hello world!")