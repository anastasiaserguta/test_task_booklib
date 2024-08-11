from django.urls import path
from . import views
from .views import (
    home, 
    about, 
    all_authors, 
    all_books, 
    succes,
    succes_delete,
    BookSearchResultsView, 
    search, 
    AuthorSearchResultView,
    GenreSearchResultView,
    book_detail,
    author_detail,
    create,
    BookCreateView,
    AuthorCreateView,
    GenreCreateView,
    AuthorDeleteView,
    BookDeleteView,
    AuthorUpdateView,
    BookUpdateView,
)


urlpatterns = [
    path('about/', views.about, name='catalog-about'),
    path('authors/', views.all_authors, name='authors'),
    path('books/', views.all_books, name='books'),
    path('search/', views.search, name='search'),
    path('create/', views.create, name='create'),
    path('succes/', views.succes, name='succes'),
    path('delete/succes/', views.succes_delete, name='succes-delete'),
    path('create/author/', AuthorCreateView.as_view(), name='author-form'),
    path('create/genre/', GenreCreateView.as_view(), name='genre-form'),
    path('create/book/', BookCreateView.as_view(), name='book-form'),
    path('author/<str:pk>/update/', AuthorUpdateView.as_view(), name='author-update'),
    path('book/<str:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('delete/author/<str:pk>/', AuthorDeleteView.as_view(), name='author-delete'),
    path('delete/book/<str:pk>', BookDeleteView.as_view(), name='book-delete'),
    path('search/book/', BookSearchResultsView.as_view(), name='search-book'),
    path('search/author/', AuthorSearchResultView.as_view(), name='search-author'),
    path('search/genre/', GenreSearchResultView.as_view(), name='search-genre'),
    path('detail/book/<str:_id>/', views.book_detail, name='book-detail'),
    path('detail/author/<str:_id>/', views.author_detail, name='author-detail'),
    path('', views.home, name='catalog-home'),
]