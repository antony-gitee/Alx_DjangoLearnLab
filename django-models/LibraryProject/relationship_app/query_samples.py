from relationship_app.models import Book, Author, Library, Librarian

# List all books in a library
def list_books_in_library(library_id):
    return Book.objects.filter(library__id=library_id)

# Query all books by a specific author
def books_by_author(author_id):
    return Book.objects.filter(author__id=author_id)

# Retrieve the librarian for a library
def get_librarian_for_library(library_id):
    return Librarian.objects.filter(library__id=library_id).first()
