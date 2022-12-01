from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

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


class form_view(View):
    template = "form.html"
    contexto = {}
    contexto['form'] = InputForm()

    def get(self, request):
        return render(
            request=request,
            template_name=self.template,
            context=self.contexto
            )

    def post(self, request):
        print("POST")
        return HttpResponse("Index POST")