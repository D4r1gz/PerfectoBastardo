from django.urls import path
from .views import agregar_producto, carrito, eliminar_producto, home, biografia, limpiar_carrito, logout, logout_view, merchandising, discografia, galeria, formulario_registro, inicio_sesion, conciertos, modificar_evento, eliminar_evento, modificar_producto, productos_view, restar_producto, usuario
 
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
    path('logout',logout_view,name='logout'),
    path('modificar_producto/<id>', modificar_producto, name='modificar_prod'),
    path('eliminar_producto/<id>', eliminar_producto, name='eleminar_producto'),
    path('agregar_producto/<producto_id>', agregar_producto, name='agregar_producto'),
    path('restar_producto/<producto_id>', restar_producto, name='restar_producto'),
    path('limpiar_producto', limpiar_carrito, name='limpiar_carrito'),
]
