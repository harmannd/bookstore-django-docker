from django.shortcuts import render, get_object_or_404, \
    get_list_or_404

from .models import Book
from .forms import SearchForm

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            #process data
            search = form.cleaned_data['search']
            books = get_list_or_404(Book.objects.filter(Book.title==search))
    else:
        form = SearchForm()
        books = get_list_or_404(Book)[:10]
    return render(
        request,
        'bookstore_api/index.html',
        {
            'FILE_TYPES': Book.FILE_TYPES,
            'LANGUAGES': Book.LANGUAGES,
            'books': books,
            'form': form
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

def about(request):
    return render(request, 'bookstore_api/about.html')