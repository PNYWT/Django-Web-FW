from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.homePage, name ='homeMain'),
    path('Home/', views.homePage, name ='home'),
    path('About/', views.aboutPage, name ='about'),
    path('Subscription_form/', views.subcriptionFormPage, name = 'Subscription_form'),
    path('Subscription_ty/', views.subscription_ty, name = 'Subscription_ty')
]