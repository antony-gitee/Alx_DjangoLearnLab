from .models import Library, Book, Author, Librarian

# 1. List all books in a library
def list_books_in_library(library_id):
    try:
        library = Library.objects.get(id=library_id)
        books = Book.objects.filter(library=library)
        return books
    except Library.DoesNotExist:
        return []


# 2. Query all books by a specific author
def books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return []


# 3. Retrieve the librarian for a library
def get_librarian(library_id):
    try:
        library = Library.objects.get(id=library_id)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None
