from django.urls import URLPattern, path
from . import views


urlpatterns = [
    path('', views.foods, name ='Foods'),
    path('<int:food_Id>', views.foodId, name ='foodId'),
]
