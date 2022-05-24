from django.contrib import admin
from .models import TipoEvento, Evento, TipoUsuario, Usuario

# Register your models here.
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(TipoEvento)
admin.site.register(Evento)

