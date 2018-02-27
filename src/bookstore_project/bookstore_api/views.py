from django.shortcuts import render, get_object_or_404, \
    get_list_or_404
from django.http import Http404

from .models import Book
from .forms import SearchForm, FilterForm

def index(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        filter_form = FilterForm(request.POST)
        if 'search' in request.POST:
            books = get_list_or_404(Book)[:6]
        if 'filter' in request.POST and filter_form.is_valid():
            file_types = filter_form.cleaned_data.get('file_type')
            languages = filter_form.cleaned_data.get('language')
            # No file type filter
            if not file_types:
                for ftype in Book.FILE_TYPES:
                    file_types.append(ftype[0])
            # No language filter
            if not languages:
                for lang in Book.LANGUAGES:
                    languages.append(lang[0])
            # Filter results
            books = []
            for book in Book.objects.all():
                if book.file_type in file_types and book.language in languages:
                    books.append(book)
    else:
        search_form = SearchForm()
        filter_form = FilterForm()
        books = get_list_or_404(Book)[:10]
    return render(
        request,
        'bookstore_api/index.html',
        {   'Book': Book,
            'books': books,
            'search_form': search_form,
            'filter_form': filter_form
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