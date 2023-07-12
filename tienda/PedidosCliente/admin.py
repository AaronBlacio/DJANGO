from django.contrib import admin
from PedidosCliente.models import Cliente, Pedido


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "email",
        "direcion",
    )
    search_fields = ("nombre",)


# Register your models here.
admin.site.register(
    Cliente,
    ClienteAdmin,
)


class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "numero",
        "fecha",
    )
    search_fields = ("fecha",)
    date_hierarchy = "fecha"
    list_filter = ("fecha",)


admin.site.register(Pedido, PedidoAdmin)
