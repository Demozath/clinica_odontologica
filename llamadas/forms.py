from django import forms
from .models import Llamada

class LlamadaForm(forms.ModelForm):
    class Meta:
        model = Llamada
        fields = ['resultado', 'comentarios']
