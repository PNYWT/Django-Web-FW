from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import HttpResponse
from App_foods.models import FoodModel

# Create your views here.
def homePage(request):
    return render(request, 'App_general/Home.html')

def aboutPage(request):
    return render(request, 'App_general/About.html')

def subcriptionFormPage(request):
    menu_Foods = FoodModel.objects.order_by('-is_Premium')
    context = { 'menuFoods' : menu_Foods}
    return render(request, 'App_general/Subcription_form.html', context)

def subcription_ty(request):
    return render(request, 'App_general/Subcription_ty.html')