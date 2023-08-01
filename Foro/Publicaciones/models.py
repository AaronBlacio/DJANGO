from django.db import models

# Create your models here.
class Publicacion(models.Model):
    nombre_autor = models.CharField(max_length=100)
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateField()
    estado = models.CharField(max_length=1)
    def __str__(self):
        return 'Publicacion: {self.cnombre_autor}'