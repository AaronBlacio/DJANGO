from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre_libro = models.CharField()
    nombre_autor = models.CharField()
    categoria = models.CharField()
    precio = models.FloatField()
    codigo = models.CharField()
    estado = models.CharField(max_length=2)
    def __str__(self):
        return 'Libro: {self.cnombre_libro}'