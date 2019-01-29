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
    title = forms.CharField(required=True)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = forms.ModelMultipleChoiceField(queryset=Author.objects.all(),required=True)
    
    summary = forms.CharField(required=True)
    isbn = forms.CharField(required=True)
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = forms.ModelMultipleChoiceField(queryset=Genre.objects.all(),required=True)
    wordCount = forms.IntegerField(required=True)
    charpterCount = forms.IntegerField(required=True)
    bookFile = forms.FileField(required=True)
    class Meta:
        model = Book
        fields = ('title','author','summary','isbn','genre','wordCount','charpterCount','bookFile',)