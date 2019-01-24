
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

from application.models import Profile, Book, Marker, Author, Genre
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, UploadFileForm, UserForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

from django.contrib.auth.models import User

    
# Create your views here.
def index(request):
    context = {

    }
    return render(request, 'index.html', context=context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(username,password)
        if user is not None:
            auth_login(request, user)
            return redirect('/application')

        else:
            return HttpResponse("Invalid login details given")
    return render(request, 'login.html',{})

def signup(request):
    if request.method =='GET':
        form = SignUpForm(request.GET)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignUpForm() 
    
    return render_to_response('SignUp.html',{'form': form})



def editProfile(self,request):
    print("get request?")
    args = {}

    if request.method == 'POST':
        print('this is get')
        # form = UploadFileForm(request.POST, instance = request.user.profile)
        user_form = UserForm(request.POST, instance = request.user)
        
        if user_form.is_valid():
            # form.save()
            user_form.save()
            return redirect('/profile')
        else:
            return HttpResponse("Invalid profile editting")
    else:
        print("form is not right")
        # form = UploadFileForm(instance = request.user.profile)
        user_form= UserForm(instance = request.user)
        # args['form'] = form
        print("return render")
        # return render(request, 'profile/',{'user_form': user_form,'profile_form': profile_form})
        return render(request, 'editProfile.html',{'user_form': user_form})



class SignUpView(generic.TemplateView):
    template_name='SignUp.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        return context
    
class ProfileView(generic.TemplateView):
    template_name ='Profile.html'

class editProfileView(generic.TemplateView):
    template_name ='editProfile.html'
    print("fku")
    # def post(self,request):
    #     print("get request?")
    #     args = {}

    #     if request.method == 'POST':
    #         print('this is get')
    #         form = UploadFileForm(request.POST, instance = request.user.profile)
    #         user_form = UserForm(request.POST, instance = request.user)
            
    #         if user_form.is_valid() and form.is_valid():
    #             form.save()
    #             user_form.save()
    #             return redirect('profile')
    #         else:
    #             return HttpResponse("Invalid profile editting")
    #     else:
    #         print("form is not right")
    #         form = UploadFileForm(instance = request.user.profile)
    #         user_form= UserForm(instance = request.user)
    #         args['form'] = form
    #         print("return render")
    #         return render(request, 'profile/',{'user_form': user_form,'profile_form': profile_form})
