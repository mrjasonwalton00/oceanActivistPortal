from django.urls import path
from . import views


urlpatterns = [
    #base urls
    path('', views.homePage, name='homePage'),
    path('registerPage/', views.registerPage, name='registerPage'),

    # Register Buddy urls
    path('registerWhale/', views.registerWhale, name='registerWhale'),
    path('registerTurtle/', views.registerTurtle, name='registerTurtle'),
    path('registerSeal/', views.registerSeal, name='registerSeal'),
    path('registerDolphin/', views.registerDolphin, name='registerDolphin'),
    path('registerSeagull/', views.registerSeagull, name='registerSeagull'),

    # Portal urls





]
