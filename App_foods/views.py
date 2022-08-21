from django.http import HttpRequest
from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse


from datetime import datetime
# import List of Menu Foods
from App_foods.models import FoodModel

# List of Menu Foods
# menu_Foods = [
#     {
#         'id': 1, 'title': 'Dark Choco Premium 1 Box', 'price': 499, 'is_premium': True, 'end_Promotion':datetime(2022,7,7)
#     },
#     {
#         'id': 2, 'title': 'Red Spicy 1 Box', 'price': 349, 'is_premium': False, 'end_Promotion':datetime(2022,7,7)
#     },
#     {
#         'id': 3, 'title': 'Blue Glacier 1 Box', 'price': 349, 'is_premium': False, 'end_Promotion':datetime(2022,7,7)
#     },
#     {
#         'id': 4, 'title': 'Blue Glacier 5 Box', 'price': 1499, 'is_premium': True, 'end_Promotion':datetime(2022,7,7)
#     },

# ]

# Create your views here.

# Menu
def foods(request):
    menu_Foods = FoodModel.objects.order_by('-is_Premium')
    context = { 'menuFoods' : menu_Foods}
    return render(request, 'App_foods/Foods.html', context)

# Menu id
def foodId(request, food_Id):
    oneMenu = None
    try:
        oneMenu = FoodModel.objects.get(id=food_Id)
    except:
        print("Not Found Index Menu")
    context = { 'food' : oneMenu}
    return render(request, 'App_foods/foodId.html', context)