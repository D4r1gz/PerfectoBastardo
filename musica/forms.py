from dataclasses import fields
from pyexpat import model
from django import forms
from django.forms import ModelForm
from .models import Usuario

class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        fields=['nombreUsuario', 'Contrasenna','Fecha_nac']