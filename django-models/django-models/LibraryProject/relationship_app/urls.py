from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.list_books, name='list_books'),  # Function-Based View
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),  # Class-Based View
]
