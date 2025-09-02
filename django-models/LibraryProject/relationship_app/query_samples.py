from relationship_app.models import Book, Author, Library, Librarian

# List all books in a library
def list_books_in_library(library_id):
    books = Book.objects.filter(library_id=library_id)
    return books

# Query all books by a specific author
def books_by_author(author_id):
    books = Book.objects.filter(author_id=author_id)
    return books

# Retrieve the librarian for a library
def get_librarian_for_library(library_id):
    try:
        librarian = Librarian.objects.get(library_id=library_id)
        return librarian
    except Librarian.DoesNotExist:
        return None
