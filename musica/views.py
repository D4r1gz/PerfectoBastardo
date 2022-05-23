from ast import And
from django.shortcuts import render
from musica.models import Evento
from .forms import EventoForm

# Create your views here.

def home(request):
    listaEvento = Evento.objects.all()
    datos = {
        'evento': listaEvento
    }
    return render(request, 'musica/index.html', datos)


def discografia(request):
    return render(request, 'musica/discografia.html')
def galeria(request):
    return render(request, 'musica/galeria.html')
def formulario_registro(request):
    return render(request, 'musica/formulario_registro.html')
def inicio_sesion(request):
    return render(request, 'musica/inicio_sesion.html')
def merchandising(request):
    return render(request, 'musica/merchandising.html')
def biografia(request):
    return render(request, 'musica/biografia.html')

def conciertos(request):
    form= EventoForm()
    return render(request, 'musica/conciertos.html',{'nom_form':form}) 

def conciertos(request):
    datos = {
        'non_form':EventoForm()    
    }
    
    if(request.method == 'POST'):
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Evento registrado correctamente'
    return render(request, 'musica/conciertos.html',datos)

