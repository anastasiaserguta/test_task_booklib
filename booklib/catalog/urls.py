from django.urls import path
from . import views
from .views import home, about, all_authors, all_books


urlpatterns = [
    path('about/', views.about, name='catalog-about'),
    path('authors/', views.all_authors, name='authors'),
    path('books/', views.all_books, name='books'),
    path('', views.home, name='catalog-home'),
]