
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
from django.views.generic import ListView, DetailView, CreateView, UpdateView,TemplateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse

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


    genre1_top6_books=Book.objects.filter(genre = genres[0]).order_by('-wordCount')[:6]
    genre2_top6_books=Book.objects.filter(genre = genres[1]).order_by('-wordCount')[:6]
    genre3_top6_books=Book.objects.filter(genre = genres[2]).order_by('-wordCount')[:6]
    genre4_top6_books=Book.objects.filter(genre = genres[3]).order_by('-wordCount')[:6]
    genre5_top6_books=Book.objects.filter(genre = genres[4]).order_by('-wordCount')[:6]
    genre6_top6_books=Book.objects.filter(genre = genres[5]).order_by('-wordCount')[:6]
   
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
        print(username,password)
        if user is not None:
            
            auth_login(request, user)
            return redirect('/application')

        else:
            error='Please enter valid Username and Password.'
    return render(request, 'login.html',{'error': error})

def signup(request):
    if request.method =='GET':
        form = SignUpForm(request.GET)
        if form.is_valid():
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
            return redirect('profile')
        else:
            return redirect('edit-profile')
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
            genre = request.POST.getlist('genre')       
            wordCount = request.POST.get('wordCount')
            
            bookFile = request.POST.get('bookFile')
            bookImage= request.POST.get('bookImage')
            book = Book.objects.create()
            try:
                tempAuthor = Author.objects.get(authorName=author)
            except Author.DoesNotExist:
                tempAuthor = Author(authorName=author)
                tempAuthor.save()
            book.author = tempAuthor
            # tempGenre = Genre.objects.get(name=genre)
            # book.author = author
            # book.author = Author(authorName=author)
            # book.author.authorName=author
            # book.author.get(author)
            #book.author.authorName=author
            for i in range(len(genre)):
                book.genre.add(genre[i])   
            # print(author,authorname)
            # book.genre.add(genre)
            # book.genre = tempGenre
            book.title=title
            book.summary=summary
            book.isbn=isbn
            book.wordCount=wordCount
            
            book.bookFile=bookFile
            book.created_author= request.user
            if bookImage:
                book.bookImage= bookImage            

            book.save()
            request.user.profile.num_created_books+=1
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

        print(self.get_object().genre.all())
        
        return context
    

class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title','author', 'bookImage', 'summary', 'isbn',
            'genre', 'wordCount', 'chapterCount', 'like','date_uploaded']

class BookUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title','author', 'bookImage', 'summary', 'isbn',
            'genre', 'wordCount', 'chapterCount', 'like','date_uploaded']
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
        return context
    

class ChapterCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Marker
    fields = ['chapterId', 'content']
    book_object=None

    def get_context_data(self, **kwargs):
        context = super(ChapterCreateView, self).get_context_data(**kwargs)

        book_id= self.request.POST.get('system',None)
        book_object= Book.objects.get(id = book_id)
        ChapterCreateView.book_object= book_object
        context['book_object']= book_object


        return context

    def form_valid(self, form,**kwargs):
        self.objects = form.save(commit=False)

        self.objects.book= self.book_object
        self.objects.save()

        return super().form_valid(form)

    def test_func(self):
        
        book_object= ChapterCreateView.book_object

        if not book_object:
            book_id= self.request.POST.get('system',None)
            book_object= Book.objects.get(id = book_id)
            ChapterCreateView.book_object= book_object
        
        print(book_object.created_author)

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

        if self.request.user == chapter.book.created_author:
            return True
        return False

    def get_success_url(self):
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
    if not user.favorite.filter(pk=book_id).exists():
        user.favorite.add(book_id)
    user.save()
    next = request.GET.get('next', '/')
    return redirect(next)
def removeFavorite(request, book_id):

    user = request.user.profile
    user.favorite.remove(book_id)
    user.save()
    next = request.GET.get('next', '/')
    return redirect(next)