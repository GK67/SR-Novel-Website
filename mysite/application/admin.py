from django.contrib import admin
from application.models import Profile, Book, Favorite, Marker, Author, Genre

<<<<<<< HEAD
# Register your models here.

from application.models import Author, Profile, Genre, Book, Favorite, Marker


admin.site.register(Genre)

# admin.site.register(Author)
# Define the admin class
class BookInline(admin.TabularInline):
    model = Book
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('authorId', 'authorName')
    fields = ['authorId', 'authorName']
    inlines = [BookInline]
    
# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#admin.site.register(Book)
#admin.site.register(BookInstance)

# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('bookId', 'title', 'author', 'display_genre')

# Register the Admin classes for BookInstance using the decorator

@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status', 'due_back','id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )







admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Profile)
admin.site.register(Favorite)
admin.site.register(Marker)





=======
# Register your models here

#admin.site.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ('user', 'display_markerId','display_favoritedId', 'profile_image','about_me')
admin.site.register(Profile,ProfileAdmin)

#admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):

	list_display = ('title', 'bookId', 'title', 'authorId', 'display_genre', 'wordCount','summary', 'isbn')

admin.site.register(Book,BookAdmin)

#admin.site.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):

	list_display = ('FavoriteId', 'bookId')

admin.site.register(Favorite,FavoriteAdmin)

#admin.site.register(Marker)
class MarkerAdmin(admin.ModelAdmin):

	list_display = ('markerId', 'bookId', 'chapterId')

admin.site.register(Marker,MarkerAdmin)

#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('authorId', 'authorName')
admin.site.register(Author,AuthorAdmin)

#admin.site.register(Genre)
class GenreAdmin(admin.ModelAdmin):
	pass
admin.site.register(Genre,GenreAdmin)
>>>>>>> master
