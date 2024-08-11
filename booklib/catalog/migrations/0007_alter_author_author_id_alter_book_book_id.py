# Generated by Django 5.0.7 on 2024-08-10 12:33

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0006_alter_author_options_alter_book_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="author_id",
            field=models.UUIDField(
                default=uuid.UUID("e7f18fe9-0512-4bf7-8d92-bb74a50ca91c"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="book_id",
            field=models.UUIDField(
                default=uuid.UUID("5db7b5e6-288d-4fc9-b425-d5aae70c2415"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
