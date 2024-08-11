from django.urls import path
from . import views
from .views import (
    home, 
    about, 
    all_authors, 
    all_books, 
    BookSearchResultsView, 
    search, 
    AuthorSearchResultView,
    GenreSearchResultView,
    book_detail,
    author_detail,
)


urlpatterns = [
    path('about/', views.about, name='catalog-about'),
    path('authors/', views.all_authors, name='authors'),
    path('books/', views.all_books, name='books'),
    path('search/', views.search, name='search'),
    path('search/book/', BookSearchResultsView.as_view(), name='search-book'),
    path('search/author/', AuthorSearchResultView.as_view(), name='search-author'),
    path('search/genre/', GenreSearchResultView.as_view(), name='search-genre'),
    path('detail/book/<str:_id>/', views.book_detail, name='book-detail'),
    path('detail/author/<str:_id>/', views.author_detail, name='author-detail'),
    path('', views.home, name='catalog-home'),
]