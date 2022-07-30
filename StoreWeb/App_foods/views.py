from django.shortcuts import render
from django.http.response import HttpResponse
from datetime import datetime

# List of Menu Foods
menu_Foods = [
    {
        'id': 1, 'title': 'Dark Choco Premium 1 Box', 'price': 499, 'is_premium': True, 'end_Promotion':datetime(2022,7,7)
    },
    {
        'id': 2, 'title': 'Red Spicy 1 Box', 'price': 349, 'is_premium': False, 'end_Promotion':datetime(2022,7,7)
    },
    {
        'id': 3, 'title': 'Blue Glacier 1 Box', 'price': 349, 'is_premium': False, 'end_Promotion':datetime(2022,7,7)
    },
    {
        'id': 4, 'title': 'Blue Glacier 5 Box', 'price': 1499, 'is_premium': True, 'end_Promotion':datetime(2022,7,7)
    },
    
]

# Create your views here.

def foods(request):
    context = { 'menuFoods' : menu_Foods}
    return render(request, 'App_foods/Foods.html', context)

def foodId(request, food_Id):
    idofMune = None
    try:
        idofMune = [f for f in menu_Foods if f['id'] == food_Id][0]
    except IndexError:
        print("Not Found Index FoodId")
    context = { 'food' : idofMune}
    return render(request, 'App_foods/foodId.html', context)