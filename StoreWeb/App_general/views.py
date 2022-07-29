from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def homePage(request):
    return render(request, 'App_general/Home.html')

def aboutPage(request):
    return render(request, 'App_general/About.html')