from django.shortcuts import render, get_object_or_404, \
    get_list_or_404

from bookstore_api.models import Book


def index(request):
    books = get_list_or_404(Book)[:10]
    return render(
        request,
        'bookstore_api/index.html',
        {
            'FILE_TYPES': Book.FILE_TYPES,
            'LANGUAGES': Book.LANGUAGES,
            'books': books
        }
    )

def details(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(
        request,
        'bookstore_api/details.html',
        {
            'book': book
        }
    )