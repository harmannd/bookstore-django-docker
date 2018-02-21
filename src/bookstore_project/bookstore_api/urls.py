from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/', views.details, name='details'),
    path('about/', views.about, name='about'),
]