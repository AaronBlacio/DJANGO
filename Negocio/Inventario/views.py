from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ProductoForm, UserRegisterForm
from .models import Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index (request):
    return render(request, 'Inventario/index.html',{
        'producto': Producto.objects.all()
    })

def view_producto(request, id):
    producto=Producto.objects.get(px=id)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            nuevo_producto = form.cleaned_data['nombre']
            nuevo_precio = form.cleaned_data['precio']
            nuevo_codigo = form.cleaned_data['codigo']

            nuevoproducto = Producto(
                nombre = nuevo_producto,
                precio = nuevo_precio,
                codigo = nuevo_codigo,
                estado = 'A'
            )

            nuevoproducto.save()
            return render(request, 'inventario/add.html',{
                'form':ProductoForm(),
                'success':True
            })
    else:
        form = ProductoForm()
        return render(request,'inventario/add.html',{
            'form':ProductoForm(),
        })
    
def edita(request,id):
    if request.method == 'POST':
        producto = Producto.objects.get(pk=id)
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return render(request, 'inventario/edit.html',{
                'form':form,
                'success':True
            })
    else:
        producto = Producto.objects.get(pk=id)
        form = ProductoForm(instance=producto)

    return render(request, 'inventario/edit.html',{
        'form':form
    })

def elimina(request,id):
    if request.method == 'POST':
        producto = Producto.objects.get(pk=id)
        producto.estado='I'
        producto.save()
    return HttpResponseRedirect(reverse('index'))

from django.contrib.auth.decorators import login_required

@login_required
def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if request.is_valid():
            usuario = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Usuario {usuario} creado')
            return redirect(index)
    else:
        form = UserRegisterForm()
    contex = { 'form':form}
    return render(request, 'inventario/register.html', contex)