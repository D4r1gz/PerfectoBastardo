from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from musica.models import Evento

class eventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ['nombreEvento','descripcion','fecha','precio','categoria']