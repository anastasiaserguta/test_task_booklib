from uuid import uuid4

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField(verbose_name="Название жанра", max_length=200, blank=False)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("succes")

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(
        verbose_name="Фамилия и имя автора", max_length=100, blank=False
    )
    author_id = models.UUIDField(
        primary_key=True, default=uuid4(), null=False, unique=True, editable=False
    )
    about_author = models.TextField(
        verbose_name="Об авторе", max_length=2000, blank=True
    )

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={'_id': self.author_id})

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(verbose_name="Название книги", max_length=300, blank=False)
    author = models.ManyToManyField(Author, verbose_name="Автор")
    description = models.TextField(verbose_name="Описание", max_length=2000, blank=True)
    genre = models.ManyToManyField(Genre, verbose_name="Жанр")
    book_id = models.UUIDField(
        primary_key=True, default=uuid4(), null=False, unique=True, editable=False
    )
    release_year = models.PositiveIntegerField(
        verbose_name="Год издания",
        null=True,
        blank=True,
        validators=[MinValueValidator(800), MaxValueValidator(2050)],
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", kwargs={'_id': self.book_id})

    def display_genre(self):
        return ", ".join([genre.name for genre in self.genre.all()[:3]])

    def display_author(self):
        return ", ".join([author.name for author in self.author.all()[:3]])

    display_genre.short_description = "Genre"
    display_author.short_description = "Author"
