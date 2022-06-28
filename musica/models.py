
from calendar import Calendar, LocaleTextCalendar, TextCalendar, calendar
from enum import _auto_null
from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import AbstractUser
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
    fecha= models.DateField()
    precio = models.IntegerField(null=True, verbose_name='Precio')
    categoria = models.ForeignKey(TipoEvento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreEvento

class TipoUser(models.Model):
    id_User = models.AutoField(primary_key=True,verbose_name='Id',auto_created=True)
    tipo_User = models.CharField(max_length=50,verbose_name='tipo')

    def __str__(self):
        return self.tipo_User

class Useer(models.Model):
    iduser = models.AutoField(primary_key=True,auto_created=True,verbose_name='Id')
    nombreUser = models.CharField(max_length=50,verbose_name='nombre')
    Contrasenna = models.CharField(max_length=100, verbose_name='contrasenna')
    correo = models.EmailField(null=True)
    telefono = models.IntegerField(verbose_name='telefono',null=False)
    usuario = models.ForeignKey(TipoUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreUser
        
class Pedido(models.Model):
    idpedido = models.AutoField(primary_key=True,verbose_name='Id')
    nombrePedido= models.CharField(max_length=50,verbose_name='nombre_pedido')
    stock = models.IntegerField(verbose_name='categoria_pedido')
    precio = models.IntegerField(verbose_name='precio')
    imagen = models.ImageField()

    def __str__(self):
        return self.tipoUsu

class DetallePedido(models.Model):
    idDetalle = models.AutoField(primary_key=True,verbose_name='Id',auto_created=True)
    fechaPedido = models.DateField()
    nombre_user = models.ForeignKey(Useer, on_delete=models.CASCADE)
    cantidad= models.IntegerField(verbose_name='cantidad')
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)

    def __str__(self):
        return self.idDetalle


