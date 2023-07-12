from django.db import models


# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=400)
    email = models.EmailField(blank=True, null=True, verbose_name="Correo Electrónico")
    direcion = models.CharField(max_length=700)


class Pedido(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    estado = models.BooleanField()
