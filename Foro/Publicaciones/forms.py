from django import forms
from .models import Publicacion



class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['nombre_autor', 'titulo', 'contenido', 'fecha']
        labels = {
            'nombre_autor': 'Nombre del autor',
            'titulo': 'Título',
            'contenido': 'Contenido', 
            'fecha': 'Fecha' 
        }
        widgets = {
            'nombre_autor': forms.TextInput(attrs={'class':'form-control'}),
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'contenido': forms.TextInput(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'AAAA-MM-DD'})
        }