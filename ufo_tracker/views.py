from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello, UFO Enthusiast!")
def mama(request):
    return HttpResponse("test mama request!")
