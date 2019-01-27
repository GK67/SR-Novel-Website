
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

from application.models import Book, Marker, Author, Genre
from user_account.models import Profile
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ForgetForm, UploadFileForm
from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


    
# Create your views here.
def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'application/index.html', context=context)

class BookListView(ListView):
    model = Book
    template_name= 'application/book_list.html'
    context_object_name='booklist'
    ordering = ['-date_uploaded']

class BookDetailView(DetailView):
    model = Book

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title','author', 'book_image', 'summary', 'isbn',
            'genre', 'wordCount', 'charpterCount', 'date_uploaded']

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = Book
    fields = ['title','author', 'book_image', 'summary', 'isbn',
            'genre', 'wordCount', 'charpterCount', 'date_uploaded']

def forget_v(request):
    if request.method =='GET':
        form = ForgetForm(request.GET)
        if form.is_valid():

            email = form.cleaned_data.get('email')
            send_mail("Forget Password",
                "Here is your pass.",
                "codingrui@gmail.com",
                [email])
            return redirect('login')
    else:
        form = ForgetForm() 
    
    return render_to_response('change_password.html',{'form': form})

