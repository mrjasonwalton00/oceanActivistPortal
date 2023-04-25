from django.urls import path
from . import views


urlpatterns = [
    #base urls
    path('', views.homePage, name='homePage'),
    path('registerPage/', views.registerPage, name='registerPage'),
]
