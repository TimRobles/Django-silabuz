from django.views import View
from django.http import HttpResponse
from django.shortcuts import render

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

