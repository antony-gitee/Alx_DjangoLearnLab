
```markdown
# Update Operation

```python
from bookshelf.models import Book

# Assume 'book' is the book we created
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()
book
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
