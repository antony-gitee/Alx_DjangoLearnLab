from django.contrib import admin
from .models import Library, Book

admin.site.register(Library)
admin.site.register(Book)

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

# Helper function to check if user is Admin
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

# Admin-only view
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

