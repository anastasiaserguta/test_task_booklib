from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import JsonResponse
from .models import Genre, Book, Author
from users.models import Profile
from django.core import serializers as sel
from django.core.serializers.json import DjangoJSONEncoder
from .serializers import BookSerializer
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
        books = {'books':BookSerializer(Book.objects.all(), many=True).data}
        response = JsonResponse(books, safe=True)
        # return response
        # {'hr': json.loads(hr)}
        return render(request, 'catalog/home.html', books)
        # return response

def about(request):
        return render(request, 'catalog/about.html', {'title': 'О BookLib'})

def search(request):
        return render(request, 'catalog/search.html')

def create(request):
        return render(request, 'catalog/create.html')

def succes(request):
        return render(request, 'catalog/succes.html')

def succes_delete(request):
        return render(request, 'catalog/succes_delete.html')

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

class BookSearchResultsView(ListView):
        model = Book
        template_name = 'catalog/search_book.html'
        

        def get_queryset(self) -> QuerySet: 
                query = self.request.GET.get('q')

                object_list = Book.objects.filter(
                        Q(title__icontains=query) | Q(release_year__icontains=query) | Q(book_id__icontains=query)
                )
                return object_list
        
class AuthorSearchResultView(ListView):
        model = Author
        template_name = 'catalog/search_author.html'

        def get_queryset(self) -> QuerySet:

                query = self.request.GET.get('q')
                
                object_list = Author.objects.filter(
                        Q(name__icontains=query) | Q(author_id__icontains=query)
                )
                return object_list
        
class GenreSearchResultView(ListView):
        model = Genre
        template_name = 'catalog/search_genre.html'

        def get_queryset(self) -> QuerySet:
                
                query = self.request.GET.get('q')

                object_list = Genre.objects.filter(
                        Q(name__icontains=query)
                )        
                return object_list
        
def book_detail(request, _id):
        context = {
        'book': Book.objects.get(book_id=_id),
	}
        return render(request, 'catalog/book_detail.html', context)

def author_detail(request, _id):
        context = {
        'author': Author.objects.get(author_id=_id),
        'his_books': Book.objects.filter(author__author_id=_id),
	}
        return render(request, 'catalog/author_detail.html', context)

class AuthorCreateView(LoginRequiredMixin, CreateView):
        model = Author
        
        fields = ['name', 'about_author',]

        def form_valid(self, form):
                        return super().form_valid(form)
        
class GenreCreateView(LoginRequiredMixin, CreateView):
        model = Genre
        
        fields = ['name',]

        def form_valid(self, form):
                        return super().form_valid(form)

class BookCreateView(LoginRequiredMixin, CreateView):
        model = Book
        
        fields = ['title', 'author', 'description', 'genre', 'release_year',]

        def form_valid(self, form):
                        return super().form_valid(form)


class AuthorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Author
        success_url = '/'

        def test_func(self) -> bool:
                return True
        
class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Book
        success_url = '/'

        def test_func(self) -> bool:
                return True
        
class AuthorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Author
        fields = ['name', 'about_author',]

        def form_valid(self, form):
                return super().form_valid(form)

        def test_func(self) -> bool:
                return True
        
class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Book
        fields = ['title', 'author', 'description', 'genre', 'release_year',]

        def form_valid(self, form):
                return super().form_valid(form)

        def test_func(self) -> bool:
                return True
        
# class GenreDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#         model = Genre
#         success_url = '/'

#         def test_func(self) -> bool:
#                 return True