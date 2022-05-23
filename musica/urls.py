from django.urls import path
from .views import home, biografia, merchandising, discografia, galeria, formulario_registro, inicio_sesion, conciertos
 
urlpatterns = [
    path('', home,name="home"),
    path('discografia', discografia, name="discografia"),
    path('formulario_registro', formulario_registro, name="formulario_registro"),
    path('galeria', galeria, name="galeria"),
    path('inicio_sesion', inicio_sesion, name="inicio_sesion"),
    path('conciertos', conciertos, name="conciertos"),
    path('biografia', biografia, name="biografia"),
    path('merchandising', merchandising, name="merchandising")
]