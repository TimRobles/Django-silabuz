from django.shortcuts import render, HttpResponse
from django.views.generic import ListView

from django.urls import reverse_lazy
from vitrina.tasks import send_book
from vitrina.forms import InputForm

from vitrina.models import Books

# Create your views here.

class BooksListView(ListView):
    model = Books
    template_name = "booklist.html"
    context_object_name = 'libros'

def select_book(request, id):
    book = Books.objects.filter(id = id)
    request.session["authors"] = book[0].authors
    request.session["id"] = book[0].id
    context = {}
    context["book"] = book[0]
    context["form"] = InputForm()
    # context['url_prueba'] = reverse_lazy('myapp:formulario')
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            print("form.is_valid()", form.cleaned_data["nombre"], form.cleaned_data["email"])
            send_book.delay(form.cleaned_data["nombre"], form.cleaned_data["email"])
            return HttpResponse(form.cleaned_data["nombre"] + " " + form.cleaned_data["email"])
        else:
            print("form.is_invalid()", form.cleaned_data["nombre"], form.cleaned_data["email"])

    return render(request, "oneBook.html", context)

def author(request, id):
    context = {}
    context["author"] = request.session["authors"]
    return render(request, "author.html", context)


def pagina1(request):
    contexto = {}
    contexto['saludo'] = 'Hola, ¿como estás?'
    request.session["sesion"] = "Estoy en la sesion"
    contexto['sesion'] = request.session["sesion"]
    contexto['usuario'] = request.user
    template = 'pagina1.html'
    return render(
        request=request,
        template_name=template,
        context=contexto
        )

def pagina2(request):
    contexto = {}
    contexto['saludo'] = 'Bien, ¿y tú?'
    contexto['sesion'] = request.session["sesion"]
    contexto['usuario'] = request.user
    template = 'pagina1.html'
    return render(
        request=request,
        template_name=template,
        context=contexto
        )