from ast import And
from time import strftime
from django.shortcuts import render,redirect
from musica.models import Evento,Useer
from .forms import EventoForm,UseerForm

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
            print('valido')
            evento=Evento()
            evento.nombreEvento = formulario.cleaned_data['nombreEvento']
            evento.descripcion = formulario.cleaned_data['descripcion']
            evento.fecha = formulario.cleaned_data['fecha']
            evento.precio = formulario.cleaned_data['precio']
            evento.categoria = formulario.cleaned_data['categoria']
            formulario.save()
            datos['mensaje'] = 'Evento registrado correctamente'
        else:
            print('no valido')
            print(formulario.errors)
    return render(request, 'musica/conciertos.html',datos)

def modificar_evento(request, id):
    evento = Evento.objects.get(nombreEvento=id) 

    datos = {
        'form': EventoForm(instance=evento)
    }

    if (request.method == 'POST'):
        formulario = EventoForm(data=request.POST, instance=evento)
        if formulario.is_valid():

            formulario.save() 
            datos['mensaje'] = 'Se modifico evento'
        else:
            datos['mensaje'] = ' No se modificó evento'
            print(formulario.errors)
    return render(request,'musica\modificar_evento.html', datos)


def eliminar_evento(request, id):
    evento = Evento.objects.get(nombreEvento=id)
    evento.delete() 

    return redirect(to='home')

def usuario(request):
    datos ={
        'forma':UseerForm()
    }

    if(request.method == 'POST'):
        print("adentro")
        formulario = UseerForm(request.POST)
        if formulario.is_valid():
            print('valido')
            formulario.save()
            datos['mensaje'] = 'registro exitoso'
        else:
            print(formulario.errors)
    return render(request, 'musica/formulario_registro.html', datos)