from rest_framework import viewsets
from books.models import Book
from books.api.serializer import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer