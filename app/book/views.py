from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Book
from book import serializers


class BookViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage books in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        return self.queryset
