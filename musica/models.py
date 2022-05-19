from django.db import models
from datetime import datetime, date

# Create your models here.
class TipoEvento(models.Model):
    idEvento = models.IntegerField(primary_key=True,verbose_name='Id de Evento')
    nombreTipoEvento = models.CharField(max_length=60,verbose_name='Nombre Tipo de Evento')

    def __str__(self):
        return self.nombreTipoEvento

class Evento(models.Model):
    nombreEvento = models.CharField(max_length=60,primary_key=True, verbose_name='Nombre Evento')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    fecha = models.DateField()
    precio = models.IntegerField(null=True, verbose_name='Precio')
    categoria = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreEvento
