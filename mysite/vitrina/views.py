from django.shortcuts import render
from django.views.generic import ListView

from django.urls import reverse_lazy

from vitrina.models import Books

# Create your views here.

class BooksListView(ListView):
    model = Books
    template_name = "booklist.html"
    context_object_name = 'libros'

def select_book(request, id):
    book = Books.objects.filter(id = id)
    request.session["authors"] = book[0].authors
    context = {}
    context["book"] = book[0]
    context['url_prueba'] = reverse_lazy('myapp:formulario')
    return render(request, "oneBook.html", context)

def author(request, id):
    context = {}
    context["author"] = request.session["authors"]
    return render(request, "author.html", context)
