from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from application.models import Profile, Book, Marker, Author, Genre
from django.core.exceptions import ValidationError

from django.contrib.auth import authenticate



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required field.')
    password1 = forms.CharField(max_length=30, required=True, help_text='Required field.')
    password2 = forms.CharField(max_length=30, required=True, help_text='Required field.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=30, required=True, help_text='Required field.')
#     password = forms.CharField(max_length=30, required=True, help_text='Required field.')

#     class Meta:
#         model = User
#         fields = ('username','password')

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('about_me','profile_image')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ( 'email', 'username')

class ForgetForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email',)

class UploadBookForm(ModelForm):
    class Meta:
        model = Book
        fields = ('title','author','summary','isbn','genre','wordCount','charpterCount','bookFile',)