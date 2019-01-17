from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    def __str__(self):
        """String for representing the Model object."""
        return self.name
class Author(models.Model):
    """Model representing an author."""
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    

   
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.authorUser.get_username()

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    wordCount = models.IntegerField(default=0)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    

    profile_image = models.FileField(blank=True, null=True)

    location = models.CharField(max_length = 25, blank=True, null=True)

    about_me = models.TextField(blank=True, null=True)

    favorites = models.ManyToManyField('Book', blank=True)

    recentPlayed = models.ManyToManyField('Book',blank=True,related_name='listeners')
    def __str__(self):
        return self.user.get_username()
    def __str__(self):
        return self.user.get_full_name()
    def __str__(self):
        return self.user.email()

    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])