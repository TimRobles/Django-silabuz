from django.shortcuts import render
from django.views.generic import ListView

from vitrina.models import Books

# Create your views here.

class BooksListView(ListView):
    model = Books
    template_name = "booklist.html"
    context_object_name = 'libros'
