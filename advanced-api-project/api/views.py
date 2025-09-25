from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer


# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    """
    List all books (read-only, accessible to everyone).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve details of a single book by its ID.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book (restricted to authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Update an existing book (restricted to authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book (restricted to authenticated users).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
