from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render


def Hola(request):
    return HttpResponse("<html><boby><h1>Durísimo el Django</h1></boby></html>")


def Chao(request):
    nombre = "Aaron"
    variable = (
        """
    <html>
        <boby>
            Hasta luego <h1> %a </h1>
        </boby>
    </html>

    """
        % nombre
    )
    return HttpResponse(variable)


def fecha(request, valor):
    edad = 19
    periodo = valor - 2023
    periodo = periodo + edad
    variable = """
    <html>
        <boby>
            tú en el año %g vas a tener %i
        </boby>
    </html>
    """ % (
        valor,
        periodo,
    )
    return HttpResponse(variable)


def plantilla(request):
    # valor = "Aaron"
    # lista = ["Blacio", "Siguenza", "Sarango", "Bonilla", "Landín"]
    # lista = []
    # documento = open("C:/Users/PC02/Documents/DJANGO/Proyecto/Proyecto/plantillas/archivo.html")
    # plt = Template(documento.read())
    # documento.close()
    # ctx = Context({"nombre": valor,"apellido": "Blacio","lista": lista,})
    # documento = plt.render(ctx)

    # documento = loader.get_template("archivo.html")
    # documento = documento.render()
    lista = [
        "Inicio",
        "Nosotros",
        "Colaboradores",
        "Labor Social",
        "Noticias",
        "Emprendimientos",
    ]
    return render(request, "contacto.html", {"lista": lista})
