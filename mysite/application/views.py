
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

from application.models import Profile, Book, Marker, Author, Genre
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.views import generic
from django.contrib.auth import login, authenticate
# from .forms import RegistrationForm
from .forms import SignUpForm
from django.contrib.auth import login as auth_login

# def register(request):
#     if request.method == 'GET':
#         f = RegistrationForm(request.GET)
#         if f.is_valid():
#             f.save()
#             username=f.cleaned_data.get('username')
#             raw_password=f.cleaned_data.get('password2')
            
            
#             user = authenticate(username=username,password=raw_password)
#             login(request,user)        
#             return redirect('/')

#     else:
#         f = RegistrationForm()

#         return render(request, 'SignUp.html', {'form': f}) 


    
# Create your views here.
def index(request):
	context = {

	}
	return render(request, 'index.html', context=context)

def login(request):
	context = {

	}
	return render(request, 'login.html', context=context)

def signup(request):
    if request.method =='GET':
        form = SignUpForm(request.GET)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('/application')
    else:
	    form = SignUpForm() 
	
    return render_to_response('SignUp.html',{'form': form})



class SignUpView(generic.TemplateView):
    template_name='SignUp.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        return context

    # def register(request):
    #     if request.method == 'GET':
    #         f = RegistrationForm(request.GET)
    #         if f.is_valid():
    #             f.save()
    #             username=f.cleaned_data.get('username')
    #             raw_password=f.cleaned_data.get('password2')
	            
	            
    #             user = authenticate(username=username,password=raw_password)
    #             login(request,user)        
    #             return redirect('/')

    #     else:
    #         f = RegistrationForm()

    #         return render(request, 'SignUp.html', {'form': f}) 