from django.contrib import admin
from application.models import Profile, Book, Marker, Author, Genre

# Register your models here

#admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'display_markerId','display_favoritedId', 'profile_image','about_me')
admin.site.register(Profile,ProfileAdmin)

#admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):

	list_display = ('title', 'display_author','chapterCount','id', 'display_genre', 'wordCount','summary', 'isbn','bookFile')

admin.site.register(Book,BookAdmin)

#admin.site.register(Marker)
class MarkerAdmin(admin.ModelAdmin):

	list_display = ('id', 'display_book', 'chapterId')

admin.site.register(Marker,MarkerAdmin)

#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('id', 'authorName')
admin.site.register(Author,AuthorAdmin)

#admin.site.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	pass
admin.site.register(Genre,GenreAdmin)
