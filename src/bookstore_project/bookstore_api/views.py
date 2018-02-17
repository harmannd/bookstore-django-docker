from django.shortcuts import render


def index(request):
    return render(request, 'bookstore_api/base.html')

