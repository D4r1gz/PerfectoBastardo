from django.contrib import admin
from .models import DetallePedido, Pedido, TipoEvento, Evento,User,TipoUser,Usuario

# Register your models here.

admin.site.register(TipoEvento)
admin.site.register(Evento)
admin.site.register(User)
admin.site.register(TipoUser)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Usuario)

