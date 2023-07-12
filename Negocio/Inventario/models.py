from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField()
    precio = models.FloatField()
    codigo = models.CharField()
    estado = models.CharField(max_length=2)
    def __str__(self):
        return 'Producto: {self.cnombre}'