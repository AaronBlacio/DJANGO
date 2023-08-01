from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Publicacion
from .forms import PublicacionForm

# Create your views here.
def index (request):
    return render(request, 'Publicaciones/index.html',{
        'publicacion': Publicacion.objects.all()
    })

def add(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid():
            nuevo_nombre_autor = form.cleaned_data['nombre_autor']
            nuevo_titulo = form.cleaned_data['titulo']
            nuevo_contenido = form.cleaned_data['contenido']

            nuevapublicacion = Publicacion(
                nombre_autor = nuevo_nombre_autor,
                titulo = nuevo_titulo,
                contenido = nuevo_contenido,
                estado = 'A'
            )
            nuevapublicacion.save()
            return render(request, 'publicaciones/add.html',{
                'form':PublicacionForm(),
                'success':True
            })
    else:
        form = PublicacionForm()
        return render(request,'publicaciones/add.html',{
            'form':PublicacionForm(),
        })