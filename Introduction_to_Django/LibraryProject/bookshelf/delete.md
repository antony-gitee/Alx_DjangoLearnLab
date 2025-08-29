
```markdown
# Delete Operation

```python
from bookshelf.models import Book

# Assume 'book' is the book we created
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Check all books
Book.objects.all()
# Output: <QuerySet []>
