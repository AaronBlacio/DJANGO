from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'codigo']
        labels = {
            'nombre': 'Producto',
            'precio': 'Precio',
            'codigo': 'Codigo'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'precio': forms.NumberInput(attrs={'class':'form-control'}),
            'codigo': forms.TextInput(attrs={'class':'form-control'})
        }

Class