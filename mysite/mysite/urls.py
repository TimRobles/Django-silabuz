"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp.views import alumno_view, aula_view, form_alumno, form_view, index_view

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("", index_view, name="home"),
    path("", index_view.as_view(), name="home"),
    path("formulario/", form_view.as_view(), name="formulario"),
    # path("formulario/", form_view, name="formulario"),
    path("formulario/<aula>/", aula_view, name="aula"),
    
    path("formAlum/", form_alumno.as_view(), name="formulario_alumno"),
    path("formAlum/<alumno>/", alumno_view, name="alumno"),
]
