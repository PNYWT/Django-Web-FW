from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.homePage, name ='homeMain'),
    path('Home/', views.homePage, name ='home'),
    path('About/', views.aboutPage, name ='about')
]