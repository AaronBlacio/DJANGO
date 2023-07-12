from django.shortcuts import render
from django.http import HttpResponse
from PedidosCliente.models import Cliente 
from PedidosCliente.forms import Contactanos
from django.core.mail import send_mail

# Create your views here.
def busca(request):
    return render(request,"buscar.html")

def encontrar(request):
    if request.GET["producto"]:
        #mensaje = " Se buscará %a " %request.GET["producto"]
        producto = request.GET["producto"]
        cliente = Cliente.objects.filter(nombre__icontains = producto)
        return render(request,"encontrado.html",{"clientes":cliente,"query":producto})
    else:
        mensaje = " No hay nada we"
    return HttpResponse(mensaje)

def contactos(request):
    if request.method=="POST":
            contacto = Contactanos(request.POST)
            if contacto.is_valid():
                informacion = contacto.cleaned_data
                send_mail(informacion['asunto'],informacion['mensaje'],informacion.get('destinatario',''),['aaronblacio12@gmail.com'],)
                return render(request, "gracias.html")
    else:
         contacto=Contactanos
    return render(request, "contacto.html",{"contacto":contacto})