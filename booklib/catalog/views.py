from django.shortcuts import render
from django.http import JsonResponse
from .models import Genre, Book, Author
from django.core import serializers as sel
from django.core.serializers.json import DjangoJSONEncoder
from .serializers import BookSerializer
import json




def home(request):
        books = {'books':BookSerializer(Book.objects.all(), many=True).data}
        response = JsonResponse(books, safe=True)
        # return response
        # {'hr': json.loads(hr)}
        return render(request, 'catalog/home.html', books)
        # return response

def about(request):
        return render(request, 'catalog/about.html', {'title': 'О BookLib'})

def all_authors(request):
        context = {
                'authors': Author.objects.all(),
        }
        return render(request, 'catalog/authors.html', context)

def all_books(request):
        context = {
                'books': Book.objects.all(),
        }
        return render(request, 'catalog/books.html', context)
