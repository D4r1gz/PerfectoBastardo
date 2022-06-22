
from calendar import Calendar, LocaleTextCalendar, TextCalendar, calendar
from django.db import models
from datetime import datetime, date

from django.forms import DateInput, DateTimeInput

from perfectoBastardo.settings import TIME_ZONE
# Create your models here.

class TipoUsuario(models.Model):
    idtipo_Usu = models.IntegerField(primary_key=True,verbose_name='Id')
    tipoUsu = models.CharField(max_length=50,verbose_name='tipo')

    def __str__(self):
        return self.tipoUsu

class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreUsuario = models.CharField(max_length=50,verbose_name='nombre')
    Contrasenna = models.CharField(max_length=6, verbose_name='contrasenna')
    Fecha_nac = models.DateField()
    usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreUsuario

class TipoEvento(models.Model):
    idEvento = models.IntegerField(primary_key=True,verbose_name='Id de Evento')
    nombreTipoEvento = models.CharField(max_length=60,verbose_name='Nombre Tipo de Evento')

    def __str__(self):
        return self.nombreTipoEvento
class Evento(models.Model):

    nombreEvento = models.CharField(max_length=60,primary_key=True, verbose_name='Nombre Evento')
    descripcion = models.CharField(max_length=300, verbose_name='Descripción')
    fecha= models.DateField(null=True)
    precio = models.IntegerField(null=True, verbose_name='Precio')
    categoria = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreEvento



