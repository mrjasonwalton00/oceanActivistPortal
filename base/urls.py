from django.urls import path
from . import views


urlpatterns = [
    #base urls
    path('', views.homePage, name='homePage'), #url for home page
    path('logout/', views.logoutUser, name='logout'), #url for logout function 
    path('registerPage/', views.registerPage, name='registerPage'), #url for register page
    


    # Register Buddy urls
    path('registerWhale/', views.registerWhale, name='registerWhale'),
    path('registerTurtle/', views.registerTurtle, name='registerTurtle'),
    path('registerSeal/', views.registerSeal, name='registerSeal'),
    path('registerDolphin/', views.registerDolphin, name='registerDolphin'),
    path('registerSeagull/', views.registerSeagull, name='registerSeagull'),


    # Portal urls
    path('portalPage/', views.portalPage, name='portalPage'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'), #url to delete post


    
]   







