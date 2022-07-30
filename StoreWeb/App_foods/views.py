from django.shortcuts import render
from django.http.response import HttpResponse

# List of Menu Foods
menu_Foods = [
    {
        'id': 1, 'title': 'Dark Choco Premium', 'price': 499, 'is_premium': True
    },
    {
        'id': 2, 'title': 'Red Spicy', 'price': 349, 'is_premium': False
    },
    {
        'id': 3, 'title': 'Blue', 'price': 349, 'is_premium': False
    }
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