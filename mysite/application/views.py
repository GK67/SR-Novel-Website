
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response

from application.models import Profile, Book, Marker, Author, Genre
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ForgetForm, EditProfileForm,UserForm,UploadBookForm

from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth import logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

    
# Create your views here.
def index(request):
    books= Book.objects.all()

    top4_books=books[:4]
    num4_list=[1,2,3,4,]
    zip_top4= zip(num4_list, top4_books)


    top10_books=books[:10]
    num10_list=[1,2,3,4,5,6,7,8,9,10,]
    zip_top10= zip(num10_list, top10_books)


    genres= Genre.objects.all()
    num6_list=[1,2,3,4,5,6,]

    context = {
        'genreAll': genres,
        'top10_books': zip_top10,
        'top4_books': zip_top4,
    }

    genre1_top6_books=Book.objects.filter(genre = genres[0]).order_by('-wordCount')[:6]
    genre2_top6_books=Book.objects.filter(genre = genres[1]).order_by('-wordCount')[:6]
    genre3_top6_books=Book.objects.filter(genre = genres[2]).order_by('-wordCount')[:6]
    genre4_top6_books=Book.objects.filter(genre = genres[3]).order_by('-wordCount')[:6]
    genre5_top6_books=Book.objects.filter(genre = genres[4]).order_by('-wordCount')[:6]
    genre6_top6_books=Book.objects.filter(genre = genres[5]).order_by('-wordCount')[:6]
    context['genre1']=genre1_top6_books
    context['genre2']=genre2_top6_books
    context['genre3']=genre3_top6_books
    context['genre4']=genre4_top6_books
    context['genre5']=genre5_top6_books
    context['genre6']=genre6_top6_books

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
            return redirect('index')
    else:
        form = SignUpForm() 
    
    return render_to_response('SignUp.html',{'form': form})

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

def edit_profile(request):
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, instance = request.user.profile)
        user_form = UserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save() 
            # pk = request.user.pk
            # pk = str(pk)
            return redirect('index')
    else:
        profile_form = EditProfileForm(instance = request.user.profile)
        user_form=UserForm(instance = request.user)
        return render(request,'edit_profile.html', {'user_form': user_form,'profile_form': profile_form})

def logout_view(request):
    logout(request)
    return redirect('index')

def upload_book(request):
    if request.method == 'POST':
        book_form = UploadBookForm(request.POST, instance = request.user)
        
        

        
        if book_form.is_valid():
            title = request.POST.get('title')
            author = request.POST.get('author')        
            summary = request.POST.get('summary')
            isbn = request.POST.get('isbn')
            genre = request.POST.get('genre')       
            wordCount = request.POST.get('wordCount')
            chapterCount = request.POST.get('chapterCount')
            bookFile = request.POST.get('bookFile')
            book = Book.objects.create()
            # book.author = author
            book.author = Author(authorName=author)
            # book.author.authorName=author
            # book.author.get(author)
            book.author.save()
            book.genre.set(genre)
            
            book.title=title
            book.summary=summary
            book.isbn=isbn
            book.wordCount=wordCount
            book.chapterCount=chapterCount
            book.bookFile=bookFile
            book.save()
            
            book_form.save()
            
           
            return redirect('profile')
    else:
        book_form = UploadBookForm(request.POST, instance = request.user)
        
        return render(request,'upload_book.html', {'book_form': book_form})


class SignUpView(generic.TemplateView):
    template_name='SignUp.html'

    def get_context_data(self, **kwargs):
        context = super(SignUpView, self).get_context_data(**kwargs)
        return context
    
class ProfileView(generic.TemplateView):
    model = Profile
    template_name ='Profile.html'
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context

class editProfileView(generic.TemplateView):
    template_name ='editProfile.html'


class BookListView(ListView):
    model = Book
    template_name= 'application/book_list.html'
    context_object_name='booklist'
    ordering = ['-date_uploaded']
    paginate_by = 5

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