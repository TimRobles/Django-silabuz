from django.contrib import admin
from .models import Salon, Alumno

# Register your models here.

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'aula',
        'hora_entrada',
        )

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'idSalon',
        )