from django import forms
from .models import Libro


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre_libro', 'nombre_autor', 'categoria', 'precio', 'codigo']
        labels = {
            'nombre_libro': 'Nombre del libro',
            'nombre_autor': 'Nombre del autor',
            'categoria': 'Categoría',
            'precio': 'Precio',
            'codigo': 'Código'
            
        }
        widgets = {
            'nombre_libro': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_autor': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'})
        }
