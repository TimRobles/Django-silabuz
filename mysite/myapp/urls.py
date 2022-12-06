from django.urls import path

from myapp.views import alumno_view, aula_view, form_alumno, form_profesor, form_view, index_view, profesor_view

app_name = 'myapp'

urlpatterns = [
    path("", index_view.as_view(), name="onlyAuthor"),
    path("formulario/", form_view.as_view(), name="formulario"),
    path("formulario/<aula>/", aula_view, name="aula"),
    
    path("formAlum/", form_alumno.as_view(), name="formulario_alumno"),
    path("formAlum/<alumno>/", alumno_view, name="alumno"),

    path("formProf/", form_profesor.as_view(), name="formulario_profesor"),
    path("formProf/<profesor>/", profesor_view, name="profesor"),

]