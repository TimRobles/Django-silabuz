from django import forms

class InputForm(forms.Form):
    aula = forms.CharField(max_length=3)
    hora_entrada = forms.TimeField(
            help_text='Ingrese la hora en formato HH:MM',
            label='Hora de la Entrada'
        )

    
class AlumnoForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    idSalon = forms.IntegerField()
