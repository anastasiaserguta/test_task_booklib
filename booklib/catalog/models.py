from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator
from uuid import uuid4


class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='введите жанр книги', blank=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    
class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, help_text='введите автора')
    author_id = models.UUIDField(primary_key=True, default=uuid4(), null=False, unique=True, editable=False)
    about_author = models.TextField(max_length=2000, help_text='об авторе', blank=True)

    class Meta:
        ordering = ['name']

    # def get_absolute_url(self):
    #     return reverse('author-detail')

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=300, blank=False, help_text='введите название книги')
    author = models.ManyToManyField(Author)
    description = models.TextField(max_length=2000, help_text='введите описание книги', blank=True)
    genre = models.ManyToManyField(Genre, help_text='укажите жанр книги')
    book_id = models.UUIDField(primary_key=True, default=uuid4(), null=False, unique=True, editable=False)
    release_year = models.PositiveIntegerField(blank=True, validators=[MinValueValidator(800), MaxValueValidator(2050)], help_text='введите год выпуска книги (при его наличии)')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join([ genre.name for genre in self.genre.all()[:3]])
    
    def display_author(self):
        return ', '.join([ author.name for author in self.author.all()[:3]])
    
    
    display_genre.short_description = 'Genre'
    display_author.short_description = 'Author'

    

