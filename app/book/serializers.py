"""Serializer for book module"""
from rest_framework import serializers
from core.models import Book


class BookSerializer(serializers.ModelSerializer):
    """Serializer for the book object"""

    class Meta:
        model = Book
        fields = ('id', 'isbn', 'title', 'authors',
                  'published_date', 'pages', 'image')
        read_only_fields = ('id',)
