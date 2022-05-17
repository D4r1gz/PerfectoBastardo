from ast import And
from django.shortcuts import render
from .models import TipoUsuario, Usuario
from .forms import UsuarioForm

# Create your views here.

def home(request):
        listaUsuario = Usuario.objects.all()
        datos = {
            'usuario': listaUsuario
        }
        return render(request,'musica/index.html', datos)
    
def discografia(request):
    return render(request, 'musica/discografia.html')
def galeria(request):
    return render(request, 'musica/galeria.html')
def formulario_registro(request):
    return render(request, 'musica/formulario_registro.html')
def inicio_sesion(request):
    return render(request, 'musica/inicio_sesion.html')
def form_usuario(request):
    form=UsuarioForm()
    return render(request, 'musica/formulario_registro.html',{'form':form})
