from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from application.models import Profile, Book, Favorite, Marker, Author, Genre
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import RegistrationForm
def register(request):
    if request.method == 'GET':
        f = RegistrationForm(request.GET)
        if f.is_valid():
            f.save()
            username=f.cleaned_data.get('username')
            raw_password=f.cleaned_data.get('password2')
            
            
            user = authenticate(username=username,password=raw_password)
            login(request,user)        
            return redirect('/')

    else:
        f = RegistrationForm()

        return render(request, 'SignUp.html', {'form': f}) 


    
# Create your views here.
def index(request):
	context = {

	}
	return render(request, 'index.html', context=context)


class LoginView(generic.TemplateView):
    template_name='login.html'

class SignUpView(generic.TemplateView):
    template_name='SignUp.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        return context

    def register(request):
        if request.method == 'GET':
            f = CustomUserCreationForm(request.GET)
            if f.is_valid():
                f.save()
                messages.success(request, 'Account created successfully')
            
                return redirect('/index')
 
        else:
            f = CustomUserCreationForm()
 
        return render(request, 'index.html', {'form': f})