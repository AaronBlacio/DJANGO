from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Libro







# Create your views here.
def index (request):
    return render(request, 'Inventario/index.html',{
        'libro': Libro.objects.all()
    })

def view_producto(request, id):
    libro=Libro.objects.get(px=id)
    return HttpResponseRedirect(reverse('index'))