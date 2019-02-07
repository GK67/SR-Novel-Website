from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordChangeForm
from application.models import Profile, Book, Marker, Author, Genre
from django.core.exceptions import ValidationError

from django.contrib.auth import authenticate



class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True, help_text='Required field.')
    password1 = forms.CharField(max_length=30, required=True, help_text='Required field.')
    password2 = forms.CharField(max_length=30, required=True, help_text='Required field.')
    email = forms.EmailField(required=True,max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

    def clean_email(self):
        
        email_data = self.cleaned_data.get('email')
        email_data=email_data.lower()
        if User.objects.filter(email=email_data).exists():
            raise forms.ValidationError("This email already used")
        return email_data

# class LoginForm(AuthenticationForm):
#     username = forms.CharField(max_length=30, required=True, help_text='Required field.')
#     password = forms.CharField(max_length=30, required=True, help_text='Required field.')

#     class Meta:
#         model = User
#         fields = ('username','password')

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('about_me',)
    def has_changed(self, *args, **kwargs):
        return True

class EditProfileImageForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_image',)
    def has_changed(self, *args, **kwargs):
        return True 

class UserForm(forms.ModelForm):
    email = forms.EmailField(required=True ,max_length=254, help_text='Required and Unique. Inform a valid email address.')
    username = forms.CharField(required=True ,help_text='Unique name or Unchanged name')
    class Meta:
        model = User
        fields = ( 'email', 'username')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email= email.lower();
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email 
    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username
    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data('email')
        user.username = self.cleaned_data('username')

        
        user.username.save()
        user.email.save()

        return user
    def has_changed(self, *args, **kwargs):
        return True
# class PasswordChangeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('password',)

class ForgetForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('email',)

class UploadBookForm(forms.ModelForm):
    author = forms.CharField(max_length=200)
    title = forms.CharField(required=True)
    bookImage =forms.FileField(required = False)
    class Meta:
        model = Book
        fields = ('title','author', 'summary', 'isbn',
            'genre', 'wordCount', 'bookImage','bookFile')
        # fields = ('title','author','summary','isbn','genre','wordCount','chapterCount','bookFile',)