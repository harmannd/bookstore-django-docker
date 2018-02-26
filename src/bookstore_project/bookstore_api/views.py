from django.shortcuts import render, get_object_or_404, \
    get_list_or_404

from .models import Book
from .forms import SearchForm, FilterForm

def index(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        filter_form = FilterForm(request.POST)
        if 'search' in request.POST:
            #books = get_list_or_404(Book.objects.filter(Book.title==search))
            books = get_list_or_404(Book)[:6]
        #if a filter is selected
        elif 'filter' in request.POST and filter_form.is_valid():
            #determine which file_types
            file_types = filter_form.cleaned_data.get('file_type')
            books = get_list_or_404(Book.objects.filter(Book.file_type in file_types))[:12]
        else:
            #nothing filtered or searched
            books = get_list_or_404(Book)[:10]
    else:
        search_form = SearchForm()
        filter_form = FilterForm()
        books = get_list_or_404(Book)[:10]
    return render(
        request,
        'bookstore_api/index.html',
        {
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