from django.db import models

# Author model
class Author(models.Model):
    """
    Author model represents a book author.
    Each author can have multiple books.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Book model
class Book(models.Model):
    """
    Book model represents a book.
    Each book belongs to a single Author.
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
