from django.urls import path
from .views import carrito, home, biografia, merchandising, discografia, galeria, formulario_registro, inicio_sesion, conciertos, modificar_evento, eliminar_evento, productos_view, usuario
 
urlpatterns = [
    path('', home,name="home"),
    path('discografia', discografia, name="discografia"),
    path('formulario_registro', usuario, name="formulario_registro"),
    path('galeria', galeria, name="galeria"),
    path('inicio_sesion', inicio_sesion, name="inicio_sesion"),
    path('conciertos', conciertos, name="conciertos"),
    path('biografia', biografia, name="biografia"),
    path('merchandising', productos_view, name="merchandising"),
    path('modificar_evento/<id>', modificar_evento, name='form_mod_evento'),
    path('eliminar_evento/<id>', eliminar_evento, name='form_ele_evento'),
    path('carrito', carrito, name='carrito'),
]