from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from musica.models import Evento, Useer
from django.contrib.auth import password_validation, authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class eventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['nombreEvento','descripcion','fecha','precio','categoria']

class useerSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields = ['username','password','token']
