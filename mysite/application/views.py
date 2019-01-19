from django.shortcuts import render
from application.models import Profile, Book, Favorite, Marker, Author, Genre

# Create your views here.
def index(request):
	context = {
	
	}
	return render(request, 'index.html', context=context)