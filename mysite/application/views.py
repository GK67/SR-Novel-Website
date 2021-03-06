
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.core.files.storage import FileSystemStorage
from application.models import Profile, Book, Marker, Author, Genre,User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ForgetForm, EditProfileForm,UserForm,UploadBookForm,EditProfileImageForm

from django.contrib.auth import login as auth_login
from django.contrib import messages
from django.core.mail import send_mail

from django.contrib.auth import logout
from django.views.generic import ListView, DetailView, CreateView, UpdateView,TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django import forms
from django.shortcuts import get_object_or_404

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
        'top_book4':top4_books,
        'genreAll': genres,
        'top10_books': zip_top10,
        'top4_books': zip_top4,
    }


    genre1_top6_books=Book.objects.filter(genre = genres[0]).order_by('-like','wordCount')[:6]
    genre2_top6_books=Book.objects.filter(genre = genres[1]).order_by('-like','wordCount')[:6]
    genre3_top6_books=Book.objects.filter(genre = genres[2]).order_by('-like','wordCount')[:6]
    genre4_top6_books=Book.objects.filter(genre = genres[3]).order_by('-like','wordCount')[:6]
    genre5_top6_books=Book.objects.filter(genre = genres[4]).order_by('-like','wordCount')[:6]
    genre6_top6_books=Book.objects.filter(genre = genres[5]).order_by('-like','wordCount')[:6]
   
    context['Horror']=genre1_top6_books
    context['Satire']=genre2_top6_books
    context['Action']=genre3_top6_books
    context['Romance']=genre4_top6_books
    context['Fantasy']=genre5_top6_books
    context['Mythology']=genre6_top6_books

    return render(request, 'index.html', context=context)


def login(request):

    error= None
    if request.user is not None and request.user.is_authenticated:
        return redirect('/application')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
       
        if user is not None:
            
            auth_login(request, user)
            return redirect('/application')

        else:
            error='Please enter valid Username and Password.'
    return render(request, 'login.html',{'error': error})

def signup(request):

    if request.user is not None and request.user.is_authenticated:
        return redirect('/application')
        
    if request.method =='GET':
        form = SignUpForm(request.GET)
   
        if form.is_valid() and form.clean_email():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            messages.success(request,'New Account %s has been created.'% (username))
            return redirect('index')
    else:
        form = SignUpForm() 
    
    return render_to_response('SignUp.html',{'form': form})

#not implement yet
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
    
    current_email= request.user.email
    if request.method == 'POST':
        profile_form = EditProfileForm(request.POST, instance = request.user.profile)
        user_form = UserForm(request.POST, instance=request.user)

        image_form = EditProfileImageForm(request.POST, request.FILES,instance= request.user.profile)
        

        if image_form.is_valid() and profile_form.is_valid() and user_form.is_valid():
            user_form.save(commit=False)
            username= user_form.cleaned_data.get('username')
            email = user_form.cleaned_data.get('email').lower();

            try:
                if current_email != email and User.objects.filter(email=email).exists():
                    raise forms.ValidationError('Email, %s, has been used, Email addresses must be unique.' % (email))
                  
                else:
                    user_form.save()
            except forms.ValidationError as e:
                messages.error(request,e)
                return redirect('application/editprofile')

            image_form.save()
            profile_form.save()
           
            return redirect('profile')
  
        else:
            return render(request,'edit_profile.html', {'user_form': user_form,'profile_form': profile_form,'image_form':image_form})
    else:
        profile_form = EditProfileForm(instance = request.user.profile)
        user_form=UserForm(instance = request.user)

        image_form = EditProfileImageForm(request.POST, instance = request.user.profile)
        return render(request,'edit_profile.html', {'user_form': user_form,'profile_form': profile_form,'image_form':image_form})


def logout_view(request):
    logout(request)
    return redirect('index')




@login_required(login_url='login/')
def upload_book(request):
    
    if request.method == 'POST':
        book_form = UploadBookForm(request.POST, request.FILES, instance = request.user)
        if book_form.is_valid():
            title = request.POST.get('title')
            author = request.POST.get('author')        
            summary = request.POST.get('summary')
            isbn = request.POST.get('isbn')
            genre = request.POST.getlist('genre')       
            
            bookFile = request.FILES.get('bookFile')
            bookImage= request.FILES.get('bookImage')
            
            book = Book.objects.create()
            try:
                tempAuthor = Author.objects.get(authorName=author)
            except Author.DoesNotExist:
                tempAuthor = Author(authorName=author)
                tempAuthor.save()
            book.author = tempAuthor
    

            for i in range(len(genre)):
                book.genre.add(genre[i])   
     

            book.title=title
            book.summary=summary
            book.isbn=isbn
            
            book.bookFile=bookFile
            book.created_author= request.user
            if bookImage:
                book.bookImage= bookImage            

            book.save()
            request.user.profile.num_created_books+=1
            book_form.save()  
            messages.success(request,
                'New Book, %s, has been created, You can go ahead to Search Your New Created Book.'% (title))
            return redirect('booklist')
    else:
        book_form = UploadBookForm(request.POST, instance = request.user)
        
        return render(request,'upload_book.html', {'book_form': book_form})


class ProfileView(LoginRequiredMixin,generic.TemplateView):
    model = Profile
    template_name ='Profile.html'
    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        return context



class BookListView(ListView):
    model = Book
    template_name= 'application/book_list.html'
    context_object_name='booklist'
    ordering = ['-date_uploaded']
    paginate_by = 5
    searchq=None
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
     
        genres = Genre.objects.all()
        context['searchq'] = BookListView.searchq

        context['genre_list']= genres
        return context

    def get_queryset(self):
        query = self.request.GET.getlist("q", None)
        link=None

        qs = Book.objects.all()

        if query != []:
            qset = Q()
            link='q='+query[0]
            for g in query[1:]:
                qset.add(Q(genre__name=g), Q.OR)
                link+='&q='+g

            qset.add(
                (Q(title__icontains = query[0]) |
                Q(author__authorName__icontains = query[0]) |
                Q(summary__icontains = query[0]) |
                Q(genre__name__icontains = query[0])),Q.AND
                )
            qs = qs.filter(qset).distinct()
        BookListView.searchq= link
 
        return qs


class BookDetailView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super(BookDetailView, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            context['favoriteBook'] = self.request.user.profile.favorite.filter(pk=context['book'].id).exists

        book_chapters= Marker.objects.filter(book= self.get_object()).order_by('id')
        self.object.chapterCount = book_chapters.count()
        self.object.save()
        context['markers']=book_chapters
        book = self.get_object()
        #print(book)
        if self.request.user == book.created_author:
            context['author'] = self.request.user
        # print(self.get_object().genre.all())
        # print(context)
        return context
    

class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title','author', 'bookImage', 'summary', 'isbn',
            'genre','bookFile']
    def test_func(self):
        book= self.get_object()
     
        if self.request.user == book.created_author:
            return True
        return False


class ChapterDetailView(DetailView):
    model = Marker

    def get_context_data(self, **kwargs):
        context = super(ChapterDetailView, self).get_context_data(**kwargs)
        if not self.request.user.is_anonymous:
            context['MarkerBook'] = self.request.user.profile.marker.filter(pk=context['marker'].id).exists
        book= self.get_object().book
        if self.request.user == book.created_author:
            context['author'] = self.request.user
        return context
    

class ChapterCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):

    model = Marker
    fields = ['chapterId', 'content']
    book_object=None

    def get_context_data(self, **kwargs):
        context = super(ChapterCreateView, self).get_context_data(**kwargs)


        book_id= self.request.POST.get('system',None)
      
        book_object= get_object_or_404(Book, pk = book_id)
        ChapterCreateView.book_object= book_object
        context['book_object']= book_object


        return context

    def form_valid(self, form,**kwargs):
        self.objects = form.save(commit=False)

        self.objects.book= self.book_object
        self.objects.save()

        self.objects.book.wordCount+= len(self.objects.content.split())
        self.objects.book.save()
    
        return super().form_valid(form)

    def test_func(self):
        
        book_object= ChapterCreateView.book_object

        if not book_object:
            book_id= self.request.POST.get('system',None)
            book_object= get_object_or_404(Book, pk=book_id)
            ChapterCreateView.book_object= book_object
        

        if self.request.user == book_object.created_author:
            return True
        return False


class ChapterUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView ):
    model = Marker
    fields = ['chapterId', 'content']

    def get_context_data(self, **kwargs):
        context = super(ChapterUpdateView, self).get_context_data(**kwargs)
        context['book_object']= self.get_object().book


        return context

    def form_valid(self, form,**kwargs):
        current_length= len(self.get_object().content.split())

        self.objects = form.save(commit=False)
        self.objects.save()

        new_length= len(self.get_object().content.split())
        total_length= self.objects.book.wordCount
        
        self.objects.book.wordCount= total_length- current_length+ new_length
        self.objects.book.save()
        
        return super().form_valid(form)

    def test_func(self):
        chapter= self.get_object()
     
        if self.request.user == chapter.book.created_author:
            return True
        return False

class ChapterDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Marker
    book_object= None
    
    def test_func(self):
        chapter= self.get_object()
        ChapterDeleteView.book_object= chapter.book
        current_length= len(self.get_object().content.split())
        #print("test_func+")
        #print(current_length)
        if self.request.user == chapter.book.created_author:
            return True
        return False

    def get_success_url(self,):
        book_id = self.kwargs['book_id']
        
        current_length= len(self.get_object().content.split())
        
        
        wordCount=self.get_object().book.wordCount
        
        wordCount = wordCount - current_length
        
        book_object= Book.objects.get(id = book_id)
        book_object.wordCount = wordCount
        
        book_object.save()
        
        return reverse('book-detail', args=[str(ChapterDeleteView.book_object.id)])




def addMarker(request,book_id,pk):

    user = request.user.profile
    MarkerId=pk
    if not user.marker.filter(pk=MarkerId).exists():
        user.marker.add(MarkerId)
    user.save()
    # print("added")
    next = request.GET.get('next', '/')
    return redirect(next)
def removeMarker(request,book_id,pk):

    user = request.user.profile
    MarkerId=pk
    user.marker.remove(MarkerId)
    user.save()
    next = request.GET.get('next', '/')
    return redirect(next)

def addFavorite(request, book_id):

    user = request.user.profile
    book_object= Book.objects.get(id = book_id)
    #print(book_object.like)
    if not user.favorite.filter(pk=book_id).exists():
        user.favorite.add(book_id)
        book_object.like=book_object.like+1
        book_object.save()
       # print(book_object.like)
    user.save()
    next = request.GET.get('next', '/')
    return redirect(next)
def removeFavorite(request, book_id):

    user = request.user.profile
    book_object= Book.objects.get(id = book_id)
    user.favorite.remove(book_id)
    book_object.like=book_object.like-1
    book_object.save()
    user.save()
    next = request.GET.get('next', '/')
    return redirect(next)