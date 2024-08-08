from django.urls import path
from . import views
from .views import home, about


urlpatterns = [
    path('', views.home, name='catalog-home'),
    path('about/', views.about, name='catalog-about'),
]