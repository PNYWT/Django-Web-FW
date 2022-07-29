from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.

def foods(request):
    return render(request, 'App_foods/Foods.html')

def foodId(request, food_Id):
    return render(request, 'App_foods/foodId.html', context={'food_Id' : food_Id})