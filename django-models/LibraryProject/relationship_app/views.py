["relationship_app/list_books.html", "Book.objects.all()"]

["relationship_app/library_detail.html", "library", "from .models import Library"]

["from django.views.generic.detail import DetailView"]

["from django.contrib.auth import login", "from django.contrib.auth.forms import UserCreationForm"]

["UserCreationForm()", "relationship_app/register.html"]

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Helper function to check if user is Admin
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin-only view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')
