from django.contrib import admin
from .models import Genre, Author, Book

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name',]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'author_id', 'about_author',]
    list_filter = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_author', 'description', 'book_id', 'release_year', 'display_genre',]
    list_filter = ('release_year', 'genre',)
