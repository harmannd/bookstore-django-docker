from django.shortcuts import render
from bookstore_api.models import Book


def index(request):
    return render(request, 'bookstore_api/base.html')
