from django import forms
#Taremos el modelo que construimos que es la tabla Tarea
from .models import Tarea


class FormTarea(forms.ModelForm):
    class Meta:
        model = Tarea
        #fields va en ingles
        fields = ['titulo','descripcion','importancia']

        #Para darle estilos a los inputs
        widgets ={
            'titulo': forms.TextInput( attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea( attrs={'class': 'form-control'}),
            'importancia': forms.CheckboxInput( attrs={'class': 'form-check-input text-center'}),
        }
