from django.shortcuts import render
from application.models import Profile, Book, Favorite, Marker, Author, Genre
from django.views import generic
# Create your views here.
def index(request):
	context = {

	}
	return render(request, 'index.html', context=context)


class LoginView(generic.TemplateView):
    template_name='login.html'

