from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello This is first project in django")

def about(request):
    return HttpResponse("I'm just copy pasting from the web! :)")

def page(request):
        return render(request, 'firstproject/index.html')