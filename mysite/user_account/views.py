from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, EditProfileForm,UserForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.views import generic


def signup(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #auth_login(request, user)
            messages.success(request, 'Account create4d for %s! You are now able to log in.' % (username))
            return redirect('login')
    else:
        form = SignUpForm() 
    
    return render(request, 'user_account/signup.html',{'form': form})

@login_required
def profile(request):
    
    return render(request, 'user_account/Profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, instance = request.user.profile)
        user_form = UserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            messages.success(request, 'Your profile has been updated') 
            # pk = request.user.pk
            # pk = str(pk)
            return redirect('index')
    else:
        profile_form = EditProfileForm(instance = request.user.profile)
        user_form=UserForm(instance = request.user)
        return render(request,'user_account/edit_profile.html', {'user_form': user_form,'profile_form': profile_form})

