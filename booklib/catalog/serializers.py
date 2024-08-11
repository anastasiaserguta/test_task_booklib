from rest_framework import serializers
from .models import Book, Author, Genre

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'author_id',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)

class BookSerializer(serializers.ModelSerializer):
        title = serializers.CharField(max_length=300)
        description = serializers.CharField(max_length=2000)
        author = AuthorSerializer(read_only=True, many=True)
        genre = GenreSerializer(read_only=True, many=True)
        book_id = serializers.CharField()
        release_year = serializers.IntegerField()

        class Meta:
            model = Book
            fields = '__all__'
