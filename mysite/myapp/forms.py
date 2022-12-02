from django import forms

class InputForm(forms.Form):
    aula = forms.CharField(max_length=3)
    hora_entrada = forms.TimeField(
            help_text='Ingrese la hora en formato HH:MM',
            label='Hora de la Entrada'
        )

    