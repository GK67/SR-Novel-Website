from django.contrib import admin
from application.models import Book, Marker, Author, Genre

# Register your models here

#admin.site.register(Profile)


#admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):

	list_display = ('title', 'id', 'display_genre', 'wordCount','summary', 'isbn')

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
