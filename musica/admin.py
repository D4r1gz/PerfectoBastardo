from django.contrib import admin
from .models import TipoEvento, Evento,TipoUser, User,Pedido,DetallePedido

# Register your models here.
admin.site.register(TipoUser)
admin.site.register(User)
admin.site.register(TipoEvento)
admin.site.register(Evento)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
