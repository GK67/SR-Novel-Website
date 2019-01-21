from django.http import HttpResponseRedirect
from django.shortcuts import render

from application.models import Profile, Book, Favorite, Marker, Author, Genre
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


from .forms import CustomUserCreationForm
 
#...
def register(request):
    if request.method == 'get':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('index')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, '/signup', {'form': f})
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

