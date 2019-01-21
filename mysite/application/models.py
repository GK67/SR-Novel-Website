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
    authorName = models.OneToOneField(User, on_delete=models.CASCADE)
    authorId = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular author')
    """bookId = models.OneToManyField()" "book of author ownered"""

   
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.authorId
class Marker(models.Model):
    """Model representing an author."""
    markerId = models.CharField(max_length=200,blank=True, null=True)
    bookId = models.CharField(max_length=200,blank=True, null=True)
    chapterId = models.CharField(max_length=200,blank=True, null=True)
    
    

   
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('Marker-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.markerId

class Favorite(models.Model):
  
    FavoriteId = models.CharField(max_length=200,blank=True, null=True)
    bookId = models.CharField(max_length=200,blank=True, null=True)

    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('Favorite-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return self.FavoriteId

class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200,blank=True, null=True)
    bookId = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    authorId = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    wordCount = models.IntegerField(default=0)

    def __str__(self):
        """String for representing the Model object."""
        return self.bookId
    def display_genre(self):

    	return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    
    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    markerId = models.ManyToManyField('Marker', blank=True)

    favoriteId = models.ManyToManyField('Favorite', blank=True)
    
    profile_image = models.FileField(blank=True, null=True)   

    about_me = models.TextField(blank=True, null=True)

    """favorites = models.ManyToManyField('Book', blank=True)

    markers = models.ManyToManyField('Marker',blank=True)"""
    def __str__(self):
        return self.user.get_username()
    def __str__(self):
        return self.user.get_full_name()
    def __str__(self):
        return self.user.email()
    def display_markerId(self):

    	return ', '.join(Marker.markerId for Marker in self.Marker.all()[:3])
    def display_favoritedId(self):

    	return ', '.join(Favorite.FavoriteId for Favorite in self.Favorite.all()[:3])
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])