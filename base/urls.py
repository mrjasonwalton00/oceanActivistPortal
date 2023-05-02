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
    
    path('profilePage/', views.profilePage, name='profilePage'),
    path('videoPage/', views.videoPage, name='videoPage'),
    path('gamePage/', views.gamePage, name='gamePage'),
    path('regAnotherBuddy/', views.regAnotherBuddy, name='regAnotherBuddy'),

    #urls to register Another Buddy
    path('registerWhale2/', views.registerWhale2, name='registerWhale2'),
    path('registerTurtle2/', views.registerTurtle2, name='registerTurtle2'),
    path('registerSeal2/', views.registerSeal2, name='registerSeal2'),
    path('registerDolphin2/', views.registerDolphin2, name='registerDolphin2'),
    path('registerSeagull2/', views.registerSeagull2, name='registerSeagull2'),



]   







