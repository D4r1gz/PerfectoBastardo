from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    idtipo_Usu = models.IntegerField(primary_key=True,verbose_name='Id')
    tipoUsu = models.CharField(max_length=50,verbose_name='tipo')

    def __str__(self):
        return self.TipoUsu

class Usuario(models.Model):
    idusuario = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreUsuario = models.CharField(max_length=50,verbose_name='nombre')
    Contrasenna = models.CharField(max_length=6, verbose_name='contrasenna')
    Fecha_nac = models.DateField()
    usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreUsuario