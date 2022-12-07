from django import forms

class InputForm(forms.Form):
    nombre = forms.CharField(max_length = 3)
    email = forms.EmailField()

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if nombre == 'KKK':
            self.add_error('nombre', 'El nombre KKK está prohibido.')
    
        return nombre