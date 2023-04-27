from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm #imports default user creation formn
from django import forms #imports django forms
from django.contrib.auth.models import User #uses the default django User model
from .models import Posts
from .models import Profile




#Form For User Registration
class CreateUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    registration_code = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'registration_code']


#Form used to register another buddy
class registerAnotherBuddy(forms.Form):
    registration_code = forms.CharField(max_length=10)

#Form Used to create a post
class createPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['postBody']


#Form used to update profile
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['firstName', 'lastName', 'age', 'bio', 'profile_picture']