from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash message
from django.contrib.auth.forms import UserChangeForm 
from .forms import CreateUserForm, registerAnotherBuddy
from django.contrib import messages 
from django.contrib.auth.models import Group 
from .models import Profile, Buddies, Posts
from django.contrib.auth.models import User


# Home Page View (login logic)
def homePage(request):
    if request.user.is_authenticated: #if we get a registered user send them to the portal
        return redirect('portalPage') #portal home page
    else:
        if request.method == 'POST': #check if we get a post request
            username = request.POST.get('username') #send username to username varible
            password = request.POST.get('password') #send password to password varible
            user = authenticate(request, username=username, password=password)
            if user is not None: #If we can see if there is a valid user
                login(request, user) #Django login method from import
                return redirect('portalPage') #sends user to the portal
            else: #if there is not a valid user
                messages.error(request, 'Username OR password is incorrect') #print flash message
        context = {}
        return render(request, 'base/homePage.html', context) #show the login page again so they can re enter the right credentials

#logout view
@login_required(login_url='homePage')
def logoutUser(request):
    logout(request) #logout method from Django import
    return redirect('homePage') # redirect user to back login page when a user logs out




def registerPage(request):
    return render(request, 'base/userReg/registerPage.html' )

# Register Buddy Views-----------------------------------------------------------------


def registerDolphin(request):
    return render(request, 'base/userReg/registerDolphin.html' )

def registerTurtle(request):
    return render(request, 'base/userReg/registerTurtle.html' )

def registerWhale(request):
    return render(request, 'base/userReg/registerWhale.html' )

def registerSeal(request):
    return render(request, 'base/userReg/registerSeal.html' )

def registerSeagull(request):
    return render(request, 'base/userReg/registerSeagull.html' )


# End of Register Buddy Views-----------------------------------------------------------



# Portal Views--------------------------------------------------------------------------
@login_required
def portalPage(request):
    return render(request, 'base/portalPages/portalPage.html' )

