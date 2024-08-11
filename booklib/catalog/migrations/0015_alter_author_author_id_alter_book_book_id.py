# Generated by Django 5.0.7 on 2024-08-11 21:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0014_alter_author_author_id_alter_book_book_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="author_id",
            field=models.UUIDField(
                default=uuid.UUID("b7ecc7b2-51d6-4073-9c54-25088734a366"),
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
                default=uuid.UUID("924df44b-4f21-4a31-8dae-92d4d8ec1b02"),
                editable=False,
                primary_key=True,
                serialize=False,
                unique=True,
            ),
        ),
    ]
