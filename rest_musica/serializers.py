from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from musica.models import Evento, Useer
from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token

class eventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['nombreEvento','descripcion','fecha','precio','categoria']

class useerSerializer(serializers.ModelSerializer):
    class Meta:
        model =Useer
        fields = ['iduser','nombreUser','Contrasenna','correo','telefono','usuario']
