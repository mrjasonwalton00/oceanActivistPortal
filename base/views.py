import os
from django.conf import settings
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout  #used for User Authentication
from django.contrib.auth.decorators import login_required #this is so we can restrict pages if you are not a logged in user
from django.contrib import messages #used to send a flash message
from django.contrib.auth.forms import UserChangeForm 
from .forms import CreateUserForm, registerAnotherBuddy, createPostForm, ProfileUpdateForm, registerAnotherBuddy
from django.contrib import messages 
from django.contrib.auth.models import Group 
from .models import Profile, Buddies, Posts
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.views import generic



# Home Page View (login logic)
@csrf_exempt
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

@csrf_exempt
def registerWhale(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'whale': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerWhale') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profile-pictures/default.jpg')
                    profile.save()

                    buddy = 'whale'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/buddy-pictures/whale.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form':form,}
        return render(request, 'base/userReg/registerWhale.html', context)


@csrf_exempt
def registerDolphin(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'dolphin': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerDolphin') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profile-pictures/default.jpg')
                    profile.save()

                    buddy = 'dolphin'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/buddy-pictures/dolphin.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form':form,}
        return render(request, 'base/userReg/registerDolphin.html', context)

@csrf_exempt
def registerTurtle(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'turtle': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerTurtle') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profile-pictures/default.jpg')
                    profile.save()

                    buddy = 'turtle'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/buddy-pictures/turtle.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form':form,}
        return render(request, 'base/userReg/registerTurtle.html', context)


@csrf_exempt
def registerSeal(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'seal': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerSeal') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profile-pictures/default.jpg')
                    profile.save()

                    buddy = 'seal'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/buddy-pictures/seal.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form':form,}
        return render(request, 'base/userReg/registerSeal.html', context)

@csrf_exempt
def registerSeagull(request):
    if request.user.is_authenticated:
        return redirect('portalPage') 
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
                if registration_code != 'seagull': # check if the registration code is correct
                    messages.error(request, 'Invalid registration code.') # send an error message
                    return redirect('registerSeagull') # redirect back to the same page
                else:
                    user = form.save()
                    group = Group.objects.get(name='premium')
                    user.groups.add(group)
                    username = user.username

                    profile = Profile.objects.create(user=user, bio='', firstName='', lastName='', age=None, profile_picture='static/images/profile-pictures/default.jpg')
                    profile.save()

                    buddy = 'seagull'
                    Buddies.objects.create(user=user, name=buddy, picture='static/images/buddy-pictures/seagull.png')

                    messages.success(request, 'Account was created for ' + username )
                    return redirect('homePage')
        context = {'form':form,}
        return render(request, 'base/userReg/registerSeagull.html', context)


# End of Register Buddy Views-----------------------------------------------------------



# Portal Views--------------------------------------------------------------------------


@login_required
@csrf_exempt
def portalPage(request):
    posts = Posts.objects.all().order_by('-date')
    user = request.user
    buddies = Buddies.objects.filter(user=user)
    if request.method == 'POST':
        # Check if the "delete_post" parameter is present in the POST request
        if 'delete_post' in request.POST:
            post_id = request.POST.get('delete_post')
            try:
                post = Posts.objects.get(id=post_id)
                # Check if the current user is the owner of the post
                if request.user == post.user:
                    post.delete()
                else:
                    return HttpResponseForbidden()
            except Posts.DoesNotExist:
                pass
        else:
            form = createPostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                postBody = post.postBody
                post.save()
                return redirect('portalPage')
    else:
        form = createPostForm()
    context = {
        'form': form,
        'posts': posts,
        'buddies': buddies,
    }
    return render(request, 'base/portalPages/portalPage.html', context)


@login_required
@csrf_exempt
def delete_post(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.user == post.user:
        post.delete()
        messages.success(request, 'Post has been deleted successfully!')
    else:
        messages.warning(request, 'You are not authorized to delete this post.')
    return redirect('portalPage')

@login_required
@csrf_exempt
def videoPage(request):
    return render(request, 'base/portalPages/videoPage.html' )

@login_required
@csrf_exempt
def gamePage(request):
    return render(request, 'base/portalPages/gamePage.html' )


# User Profile View:
@login_required
@csrf_exempt
def profilePage(request):
    # Get the current user's posts
    user_posts = Posts.objects.filter(user=request.user).order_by('-date')
    user = request.user
    buddies = Buddies.objects.filter(user=user)
    # Get the form for updating the user's profile
    form = ProfileUpdateForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            firstName = profile.firstName
            lastName = profile.lastName
            age = profile.age
            bio = profile.bio
            if 'profile_picture' in request.FILES:
                profile.profile_picture = request.FILES['profile_picture']
            profile.save()
            return redirect('profilePage')

    context = {
        'form': form,
        'user_posts': user_posts,
        'buddies': buddies,
    }
    
    return render(request, 'base/portalPages/profilePage.html', context)


@login_required
@csrf_exempt
def regAnotherBuddy(request):
    return render(request, 'base/registerAnotherBuddy/regAnotherBuddy.html' )


#Views to Register Another Buddy


@login_required
@csrf_exempt
def registerDolphin2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'dolphin': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerDolphin2') # redirect back to the same page
            else:
                # Check if user already has a 'dolphin' buddy
                if Buddies.objects.filter(user=request.user, name='dolphin').exists():
                    messages.error(request, 'You have already registered a dolphin buddy.')
                    return redirect('registerDolphin2')
                else:
                    buddy = Buddies(name='dolphin', picture='static/images/buddy-pictures/dolphin.png', user=request.user) # set the user field with the current user
                    buddy.save() # save the new Buddies instance

                    messages.success(request, 'Another buddy was registered.')
                    return redirect('portalPage')
    context = {'form': form}
    return render(request, 'base/registerAnotherBuddy/registerDolphin2.html', context)


@login_required
@csrf_exempt
def registerTurtle2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'turtle': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerTurtle2') # redirect back to the same page
            else:
                # Check if user already has a 'dolphin' buddy
                if Buddies.objects.filter(user=request.user, name='turtle').exists():
                    messages.error(request, 'You have already registered a turtle buddy.')
                    return redirect('registerTurtle2')
                else:
                    buddy = Buddies(name='turtle', picture='static/images/buddy-pictures/turtle.png', user=request.user) # set the user field with the current user
                    buddy.save() # save the new Buddies instance

                    messages.success(request, 'Another buddy was registered.')
                    return redirect('portalPage')
    context = {'form': form}
    return render(request, 'base/registerAnotherBuddy/registerTurtle2.html', context)

@login_required
@csrf_exempt
def registerSeal2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'seal': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerSealn2') # redirect back to the same page
            else:
                # Check if user already has a 'seal' buddy
                if Buddies.objects.filter(user=request.user, name='seal').exists():
                    messages.error(request, 'You have already registered a seal buddy.')
                    return redirect('registerSeal2')
                else:
                    buddy = Buddies(name='seal', picture='static/images/buddy-pictures/seal.png', user=request.user) # set the user field with the current user
                    buddy.save() # save the new Buddies instance

                    messages.success(request, 'Another buddy was registered.')
                    return redirect('portalPage')
    context = {'form': form}
    return render(request, 'base/registerAnotherBuddy/registerSeal2.html', context)


@login_required
@csrf_exempt
def registerSeagull2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'seagull': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerSeagull2') # redirect back to the same page
            else:
                # Check if user already has a 'seagull' buddy
                if Buddies.objects.filter(user=request.user, name='seagull').exists():
                    messages.error(request, 'You have already registered a seagull buddy.')
                    return redirect('registerSeagull2')
                else:
                    buddy = Buddies(name='seagull', picture='static/images/buddy-pictures/seagull.png', user=request.user) # set the user field with the current user
                    buddy.save() # save the new Buddies instance

                    messages.success(request, 'Another buddy was registered.')
                    return redirect('portalPage')
    context = {'form': form}
    return render(request, 'base/registerAnotherBuddy/registerSeagull2.html', context)

@login_required
@csrf_exempt
def registerWhale2(request):
    form = registerAnotherBuddy()
    if request.method == 'POST':
        form = registerAnotherBuddy(request.POST)
        if form.is_valid():
            registration_code = request.POST.get('registration_code') # get the value of the registration code from the form
            if registration_code != 'whale': # check if the registration code is correct
                messages.error(request, 'Invalid registration code.') # send an error message
                return redirect('registerWhale2') # redirect back to the same page
            else:
                # Check if user already has a 'whale' buddy
                if Buddies.objects.filter(user=request.user, name='whale').exists():
                    messages.error(request, 'You have already registered a whale buddy.')
                    return redirect('registerWhale2')
                else:
                    buddy = Buddies(name='whale', picture='static/images/buddy-pictures/whale.png', user=request.user) # set the user field with the current user
                    buddy.save() # save the new Buddies instance

                    messages.success(request, 'Another buddy was registered.')
                    return redirect('portalPage')
    context = {'form': form}
    return render(request, 'base/registerAnotherBuddy/registerWhale2.html', context)

    






