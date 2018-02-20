from django.shortcuts import render, get_object_or_404

from bookstore_api.models import Book


def index(request):
    return render(request, 'bookstore_api/index.html')

def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookstore_api/details.html', {'book': book})