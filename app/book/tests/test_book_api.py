"""Tests for the book api"""
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Book

from book.serializers import BookSerializer

BOOK_URL = reverse('book:book-list')


class PublicBookApiTests(TestCase):
    """Test the publicly available book api"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving books"""
        res = self.client.get(BOOK_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateBooksApiTests(TestCase):
    """Test the authorized books API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@test.com',
            'testtest'
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_books(self):
        """Get books"""
        Book.objects.create(
            isbn='0001',
            title='TEST TITLE',
            authors='BOB',
            published_date='2008',
            pages='90',
            image='https://test.com'
        )

        res = self.client.get(BOOK_URL)

        books = Book.objects.all().order_by('-title')
        serializer = BookSerializer(books, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
