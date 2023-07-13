from django import forms
from .models import Libro
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Usiario",widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label="Confirmar contraseña",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        helps_text = {k:"" for k in fields}