from rest_framework import serializers
from .models import Book   # adjust if your Book model is elsewhere

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
