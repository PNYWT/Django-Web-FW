from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.homePage, name ='homeMain'),
    path('Home/', views.homePage, name ='home'),
    path('About/', views.aboutPage, name ='about'),
    path('Subcription_form/', views.subcriptionFormPage, name = 'Subcription_form'),
    path('Subcription_ty/', views.subcription_ty, name = 'Subcription_ty')
]