from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'display_markerId','display_favoritedId', 'profile_image','about_me')
admin.site.register(Profile,ProfileAdmin)