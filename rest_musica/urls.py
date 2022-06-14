from django.urls import path
from rest_musica.views import lista_evento, detalle_evento
from rest_musica.viewsLogin import login

urlpatterns =[
    path('lista_evento', lista_evento, name="lista_evento"),
    path('detalle_evento/<eve>', detalle_evento, name='detalle_evento'),
    path('login',login,name='login'),
]