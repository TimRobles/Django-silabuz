from urllib import request
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from myapp.forms import AlumnoForm, InputForm

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
        print("Formulario GET")
        print(request.session)
        if request.GET:
            print(request.GET)
            print(request.GET.get('aula'))
            print(request.GET['aula'])
            print(request.GET['hora_entrada'])
        if request.GET:
            request.session["hora_entrada"] = request.GET['hora_entrada']
            return redirect(aula_view, aula= request.GET["aula"])
        return render(
            request=request,
            template_name=self.template,
            context=self.contexto
            )

    def post(self, request):
        print("Formulario POST")
        if request.POST:
            print(request.POST)
            print(request.POST.get('aula'))
            print(request.POST['hora_entrada'])
        if request.POST:
            request.session["hora_entrada"] = request.POST['hora_entrada']
            return redirect(aula_view, aula= request.POST["aula"])
        return render(
            request=request,
            template_name=self.template,
            context=self.contexto
            )

def aula_view(request, aula):
    hora_entrada = request.session["hora_entrada"]
    return HttpResponse(f"El parámetro enviado por URL es {aula} y recibimos del request el horario en {hora_entrada}")


# def form_view(request):
#     if request.method == "POST":
#         form = InputForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data["aula"])
#             return redirect(aula_view, aula= form.cleaned_data["aula"], horario=form.cleaned_data["hora_entrada"])

#     context = {}
#     context['form']= InputForm()
#     return render(request, "form.html", context)

def alumno_view(request, alumno):
    apellido = 'Vacio'
    try:
        apellido = request.session['apellido']
    except:
        pass
    try:
        salon = request.session['salon']
    except:
        salon = 'Vacio'
    return HttpResponse(f"Datos del alumno:<br>Nombre: {alumno}<br>Apellido:{apellido}<br>Salon:{salon}")

class form_alumno(View):
    template = 'form alumno.html'
    contexto = {}
    contexto['form'] = AlumnoForm()
    def get(self, request):
        return render(
            request=request,
            template_name=self.template,
            context=self.contexto,
            )

    def post(self, request):
        print(request.POST)
        print(request.POST['last_name'])
        print(request.POST['idSalon'])
        print(request.session)
        request.session['apellido'] = request.POST['last_name']
        request.session['salon'] = request.POST['idSalon']
        print(request.session['apellido'])
        print(request.session['salon'])
        return redirect(alumno_view, alumno=request.POST['first_name'])
