from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book.all'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book.show'), 
    path('<int:id>/review', views.review, name='book.review'), 
    path('<str:author>', views.author, name='author.books')
]
