
from wsgiref.util import request_uri
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from musica.models import Evento, Useer
from rest_musica.serializers import eventoSerializer, useerSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@csrf_exempt
@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def lista_evento(request):
    if request.method =='GET':
        listaEvento = Evento.objects.all()
        serializer = eventoSerializer(listaEvento, many= True)
        return Response(serializer.data)
    elif request.method == 'POST':
        dataP = JSONParser().parse(request)
        serializer =eventoSerializer(data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def detalle_evento(request, id):
    try:
        evento= Evento.objects.get(nombreEvento=id)
    except Evento.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        listaEvento = Evento.objects.all()
        serializer = eventoSerializer(listaEvento, many= True)
        return Response(serializer.data)
    elif request.method =="PUT":
        dataP = JSONParser().parse(request)
        serializer =eventoSerializer(evento, data=dataP)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        evento.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

