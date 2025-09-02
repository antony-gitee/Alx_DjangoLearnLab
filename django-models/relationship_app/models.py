from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    # One Author → Many Books (ForeignKey)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title} ({self.author.name})"


class Library(models.Model):
    name = models.CharField(max_length=255)
    # A Library has Many Books; a Book can be in Many Libraries
    books = models.ManyToManyField(
        Book,
        related_name="libraries",
        blank=True
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=255)
    # One Librarian ↔ One Library
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name="librarian"
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} @ {self.library.name}"

