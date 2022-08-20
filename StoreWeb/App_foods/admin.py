from django.contrib import admin
from .models import FoodModel

# Register your models here.

class FoodModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'special_Price', 'is_Premium', 'end_Promotion', 'description']
    search_fields = ['title']
    list_filter =  ['is_Premium']

admin.site.register(FoodModel, FoodModelAdmin)