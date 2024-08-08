from django.shortcuts import render
from .models import Genre, Book, Author

# Create your views here.

def home(request):
        context = {
                'books': Book.objects.all(),
        }
        return render(request, 'catalog/home.html', context)

def about(request):
        return render(request, 'catalog/about.html', {'title': 'О BookLib'})