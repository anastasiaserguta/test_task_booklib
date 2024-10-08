# Generated by Django 5.0.7 on 2024-08-11 17:11

import uuid

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0012_alter_author_about_author_alter_author_author_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="about_author",
            field=models.TextField(
                blank=True, max_length=2000, verbose_name="Об авторе"
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="author_id",
            field=models.UUIDField(
                default=uuid.UUID("d5351818-4183-4dee-9887-773b94750f44"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="author",
            name="name",
            field=models.CharField(max_length=100, verbose_name="Фамилия и имя автора"),
        ),
        migrations.AlterField(
            model_name="book",
            name="book_id",
            field=models.UUIDField(
                default=uuid.UUID("a87c4104-aad7-4c8a-80fc-250eebfd9fb4"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="description",
            field=models.TextField(
                blank=True, max_length=2000, verbose_name="Описание"
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="genre",
            field=models.ManyToManyField(to="catalog.genre", verbose_name="Жанр"),
        ),
        migrations.AlterField(
            model_name="book",
            name="release_year",
            field=models.PositiveIntegerField(
                blank=True,
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(800),
                    django.core.validators.MaxValueValidator(2050),
                ],
                verbose_name="Год издания",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="title",
            field=models.CharField(max_length=300, verbose_name="Название книги"),
        ),
    ]
