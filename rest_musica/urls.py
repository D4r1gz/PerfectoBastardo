from django.urls import path
from rest_musica.views import lista_evento, detalle_evento

urlpatterns =[
    path('lista_evento', lista_evento, name="lista_evento"),
    path('detalle_Evento/<id>', detalle_evento, name='detalle_evento')
]