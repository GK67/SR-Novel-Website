from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 

    favorite = models.ManyToManyField('application.Book')

    marker = models.ManyToManyField('application.Marker', blank=True)
    
    profile_image = models.FileField(default ='default.jpg', upload_to='profile_pics')   

    about_me = models.TextField(blank=True, null=True)

    """favorites = models.ManyToManyField('Book', blank=True)

    markers = models.ManyToManyField('Marker',blank=True)"""
    def __str__(self):
        return self.user.get_username()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img= Image.open(self.profile_image.path)

        if img.height >300 or img.width>300:
            output_size =(300, 300)
            img.thumbnaid(output_size)
            img.save(self.profile_image.path)


    def display_markerId(self):

    	return ', '.join(marker.chapterId for marker in self.marker.all()[:3])
    def display_favoritedId(self):

    	return ', '.join(favorite.title for favorite in self.favorite.all()[:3])
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])