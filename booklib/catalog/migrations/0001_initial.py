# Generated by Django 5.0.7 on 2024-08-05 20:05

import uuid

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("name", models.CharField(help_text="введите автора", max_length=100)),
                (
                    "author_id",
                    models.UUIDField(
                        default=uuid.UUID("d5ad96ed-e039-4ec6-9748-9e71842224cb"),
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "about_author",
                    models.TextField(
                        blank=True, help_text="об авторе", max_length=2000
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(help_text="введите жанр книги", max_length=200),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "title",
                    models.CharField(
                        help_text="введите название книги", max_length=300
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="введите описание книги", max_length=2000
                    ),
                ),
                (
                    "book_id",
                    models.UUIDField(
                        default=uuid.UUID("f0715fbb-7822-4392-9662-510e660048ba"),
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "release_year",
                    models.IntegerField(
                        blank=True,
                        help_text="введите год выпуска книги (при его наличии)",
                        validators=[
                            django.core.validators.MinValueValidator(800),
                            django.core.validators.MaxValueValidator(2050),
                        ],
                    ),
                ),
                ("author", models.ManyToManyField(null=True, to="catalog.author")),
                (
                    "genre",
                    models.ManyToManyField(
                        help_text="укажите жанр книги", to="catalog.genre"
                    ),
                ),
            ],
        ),
    ]
