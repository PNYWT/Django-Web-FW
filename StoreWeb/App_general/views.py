from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse
from App_foods.models import FoodModel
from . models import Subcription

# Create your views here.
def homePage(request):
    return render(request, 'App_general/Home.html')

def aboutPage(request):
    return render(request, 'App_general/About.html')

def subcriptionFormPage(request):
    if request.POST:
        # print(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        food_ids = request.POST.getlist('food_ids')
        new_sub = Subcription()
        new_sub.name = name
        new_sub.email = email
        # new_sub.save()
        # print(name)
        # print(email)
        # print(food_ids)
        return HttpResponseRedirect(reverse('Subcription_ty'))
    menu_Foods = FoodModel.objects.order_by('-is_Premium')
    context = { 'menuFoods' : menu_Foods}
    return render(request, 'App_general/Subcription_form.html', context)

def subcription_ty(request):
    return render(request, 'App_general/Subcription_ty.html')