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

class UploadFileForm(forms.ModelForm):
    about_me = forms.CharField(max_length=3000, required=False)
    
    class Meta:
<<<<<<< HEAD
        model = Profile
        fields = ('about_me',)

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=30, required=True)
	email = forms.EmailField(max_length=254,required=True)
	class Meta:
		model = User
		fields = ( 'email', 'username',)
=======
        model = User

        fields = ('username', 'ProfileImage', 'aboutMe','email')

    def clean_email(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')

        if email and User.objects.filter(email=email).exclude(username=username).count():
            raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['username']
        user.Profile.about_me = self.cleaned_data['aboutMe']
        user.Profile.profile_image = self. cleaned_data['ProfileImage']
        
        if commit:
            user.save()

        return user

class ForgetForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email',)

>>>>>>> master
