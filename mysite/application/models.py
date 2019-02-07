from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from PIL import Image
from django.core.files.storage import FileSystemStorage
# Create your models here.

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    def __str__(self):
        """String for representing the Model object."""
        return '%s' % (self.name)

class Author(models.Model):
    """Model representing an author."""
    authorName = models.CharField(max_length=200)
    """authorId = models.CharField(max_length=200,blank=True, null=True)"""
    """bookId = models.OneToManyField()" "book of author ownered"""

   
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return '%s' % (self.authorName)
class Marker(models.Model):
    """Model representing an author."""
    book = models.ForeignKey('Book', on_delete= models.CASCADE, blank=True,null=True)
    chapterId = models.CharField(max_length=200,blank=True, null=True)
    content = models.TextField(default = 'Enter content of the chapter')
    
    
    def get_absolute_url(self):
        """Returns the url to access a particular author instance."""
        return reverse('marker-detail', args=[str(self.book.id),str(self.id)])

    def display_book(self):

        return self.book.title

    def __str__(self):
        """String for representing the Model object."""
        return '%s (%s)' % (self.book,self.chapterId)


class Book(models.Model):
    """Model representing a book (but not a specific copy of a book)."""
    title = models.CharField(max_length=200,blank=True, null=True)

    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file
    author = models.ForeignKey('Author', on_delete=models.SET_NULL,blank=True, null=True)
    
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField(Genre, help_text='Select multiple genres for this book')
    wordCount = models.IntegerField(default=0)
    chapterCount = models.IntegerField(default=0,blank=True,null=True)
    bookFile = models.FileField(blank=True, null=True,upload_to='book_files')
    like = models.IntegerField(default=0,blank=True,null=True)
    date_uploaded = models.DateTimeField(default = timezone.now)
    bookImage = models.ImageField(default ='default_book.jpg', upload_to='book_images') 
    created_author= models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img= Image.open(self.bookImage.path)

        if img.height >300 or img.width>300:
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.bookImage.path)

    class Meta:
        ordering = ['-like', 'chapterCount', 'date_uploaded', '-wordCount']

    def __str__(self):
        """String for representing the Model object."""
        return '%s' % (self.title)

    

    def display_genre(self):

    	return ', '.join(genre.name for genre in self.genre.all()[:3])
    
    def display_author(self):
        if self.author is None:
            return '%s' % ("None")

        if not self.author.authorName:
            return '%s' % ("empty")
        else:
            return self.author.authorName

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])

class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    favorite = models.ManyToManyField('Book',blank=True)

    marker = models.ManyToManyField('Marker', blank=True)
    
    profile_image = models.FileField(default ='default_profile.jpg', upload_to='profile_images')   

    about_me = models.TextField(blank=True, null=True)

    num_created_books= models.IntegerField(default=0)

    


    """favorites = models.ManyToManyField('Book', blank=True)

    markers = models.ManyToManyField('Marker',blank=True)"""
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img= Image.open(self.profile_image.path)

        if img.height >300 or img.width>300:
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)

    def __str__(self):
        return self.user.get_username()

    def display_markerId(self):

    	return ', '.join(marker.chapterId for marker in self.marker.all()[:3])
    def display_favoritedId(self):

    	return ', '.join(favorite.title for favorite in self.favorite.all()[:3])
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
#code to auto update profiles for user changes
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()