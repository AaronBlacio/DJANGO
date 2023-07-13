from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Libro
from .forms import LibroForm






# Create your views here.
def index (request):
    return render(request, 'Inventario/index.html',{
        'libro': Libro.objects.all()
    })

def view_producto(request, id):
    libro=Libro.objects.get(px=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            nuevo_nombre_libro = form.cleaned_data['nombre_libro']
            nuevo_nombre_autor = form.cleaned_data['nombre_autor']
            nueva_categoria = form.cleaned_data['categoria']
            nuevo_precio = form.cleaned_data['precio']
            nuevo_codigo = form.cleaned_data['codigo']

            nuevolibro = Libro(
                nombre_libro = nuevo_nombre_libro,
                nombre_autor = nuevo_nombre_autor,
                categoria = nueva_categoria,
                precio = nuevo_precio,
                codigo = nuevo_codigo,
                estado = 'A'
            )

            nuevolibro.save()
            return render(request, 'inventario/add.html',{
                'form':LibroForm(),
                'success':True
            })
    else:
        form = LibroForm()
        return render(request,'inventario/add.html',{
            'form':LibroForm(),
        })

def edita(request,id):
    if request.method == 'POST':
        producto = Libro.objects.get(pk=id)
        form = LibroForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return render(request, 'inventario/edit.html',{
                'form':form,
                'success':True
            })
    else:
        producto = Libro.objects.get(pk=id)
        form = LibroForm(instance=producto)

    return render(request, 'inventario/edit.html',{
        'form':form
    })

def elimina(request,id):
    if request.method == 'POST':
        producto = Libro.objects.get(pk=id)
        producto.estado='I'
        producto.save()
    return HttpResponseRedirect(reverse('index'))