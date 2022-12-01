from urllib import request
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from myapp.forms import InputForm

# Create your views here.

# def index_view(request):
#     if request.method == "GET":
#         print("GET")
#         return HttpResponse("Index GET")
#     elif request.method == "POST":
#         print("POST")
#         return HttpResponse("Index POST")
#     return HttpResponse("Index")



class index_view(View):
    template = "index.html"
    contexto = {}
    contexto['name'] = 'Juan'
    contexto['last_name'] = 'Perez'
    contexto['edad'] = 25

    def get(self, request):
        print("GET")
        return render(
            request=request,
            template_name=self.template,
            context=self.contexto
            )

    def post(self, request):
        print("POST")
        return HttpResponse("Index POST")


# class form_view(View):
#     template = "form.html"
#     contexto = {}

#     def get(self, request):
#         form_get = InputForm(request.GET)
#         form_post = InputForm(request.POST)
#         self.contexto['form_get'] = form_get
#         self.contexto['form_post'] = form_post
#         return render(
#             request=request,
#             template_name=self.template,
#             context=self.contexto
#             )

#     def post(self, request):
#         print("POST")
#         form_get = InputForm(request.GET)
#         form_post = InputForm(request.POST)
#         self.contexto['form_get'] = form_get
#         self.contexto['form_post'] = form_post
#         print(form_post.cleaned_data['aula'])
#         return render(
#             request=request,
#             template_name=self.template,
#             context=self.contexto
#             )

def aula_view(request, aula, horario):
    return HttpResponse(f"El parámetro enviado por URL es {aula}, {horario}")


def form_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data["aula"])
            return redirect(aula_view, aula= form.cleaned_data["aula"], horario=form.cleaned_data["hora_entrada"])

    context = {}
    context['form']= InputForm()
    return render(request, "form.html", context)
