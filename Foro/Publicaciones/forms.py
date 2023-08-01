from django import forms
from .models import Publicacion



class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        exclude = ['fecha']
        fields = ['nombre_autor', 'titulo', 'contenido']
        labels = {
            'nombre_autor': 'Nombre del autor',
            'titulo': 'Título',
            'contenido': 'Contenido' 
        }
        widgets = {
            'nombre_autor': forms.TextInput(attrs={'class':'form-control'}),
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'contenido': forms.TextInput(attrs={'class':'form-control'})
        }