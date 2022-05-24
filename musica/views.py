from ast import And
from django.shortcuts import render,redirect
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
    datos = {
        'form':EventoForm()    
    }
    
    if(request.method == 'POST'):
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = 'Evento registrado correctamente'
    return render(request, 'musica/conciertos.html',datos)

def modificar_evento(request, id):
    evento = Evento.objects.get(nombreEvento=id) #select * from vehiculo where patente = id

    datos = {
        'form': EventoForm(instance=evento)
    }

    if (request.method == 'POST'):
        formulario = EventoForm(data=request.POST, instance=evento)
        if formulario.is_valid():
            formulario.save() #modificar a la BD
            datos['mensaje'] = 'se modifico evento'
        else:
            datos['mensaje'] = ' NO se modificó evento'

    return render(request,'musica\modificar_usuario.html', datos)


def eliminar_evento(request, id):
    evento = Evento.objects.get(nombreEvento=id)
    evento.delete() # delete from Vehiculo where patente = id

    return redirect(to='home')
