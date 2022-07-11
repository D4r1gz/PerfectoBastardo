from ast import And
import email
from lib2to3.pgen2 import token
from multiprocessing import context
from time import strftime
from django.forms import PasswordInput
from django.shortcuts import render, redirect
from musica.Carrito import Carrito
from musica.models import Evento, Pedido, Useer
from rest_musica.serializers import useerSerializer
from .forms import EventoForm, LoginForm, UseerForm, productoForm
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from django.core.paginator import Paginator, EmptyPage, InvalidPage
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


def merchandising(request):
    return render(request, 'musica/merchandising.html')


def biografia(request):
    return render(request, 'musica/biografia.html')


def carrito(request, id):
    p=Pedido.objects.get(nombrePedido=id)
    
    return render(request, 'musica/carrito.html')


def conciertos(request):
    datos = {
        'form': EventoForm()
    }

    if(request.method == 'POST'):
        formulario = EventoForm(request.POST)
        if formulario.is_valid():
            print('valido')
            evento = Evento()
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
    return render(request, 'musica/conciertos.html', datos)


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
    return render(request, 'musica\modificar_evento.html', datos)


def eliminar_evento(request, id):
    evento = Evento.objects.get(nombreEvento=id)
    evento.delete()

    return redirect(to='home')


def usuario(request):
    datos = {
        'forma': UseerForm()
    }

    if(request.method == 'POST'):
        formulario = UseerForm(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            email = formulario.cleaned_data['email']
            password_one = formulario.cleaned_data['password_one']
            password_two = formulario.cleaned_data['password_two']
            u = User.objects.create_user(
                username=usuario, email=email, password=password_one)
            u.save()
            datos['mensaje'] = 'registro exitoso'
        else:
            print(formulario.errors)
    return render(request, 'musica/formulario_registro.html', datos)


def inicio_sesion(request):
    datos = {
        'ini': LoginForm()
    }
    if (request.method == 'POST'):
        usu1 = request.POST.get('username')
        u = User.objects.get(username=usu1)
        pas = request.POST.get('password')
        token = Token.objects.get(user=u )
        useer = authenticate(request, username=usu1, password=pas, token=token)
        if useer is not None:
            login(request, useer)
            datos['mensaje'] = 'inicio exitoso'
        else:
            print(usu1, pas)
    return render(request, 'musica/inicio_sesion.html', datos)


def logout_view(request):
    logout(request)

    return render(request, 'musica/index.html')


def productos_view(request):
    lista_prod = Pedido.objects.all()
    datos={
        'productos':lista_prod
    }
    return render(request, 'musica/merchandising.html', datos)

def modificar_producto(request, id):
    producto = Pedido.objects.get(nombreEvento=id)

    datos = {
        'form_p': productoForm(instance=producto)
    }

    if (request.method == 'POST'):
        formulario = productoForm(data=request.POST, instance=producto)
        if formulario.is_valid():

            formulario.save()
            datos['mensaje'] = 'Se modifico evento'
        else:
            datos['mensaje'] = ' No se modificó evento'
            print(formulario.errors)
    return render(request, 'musica/modificar_producto.html', datos)

def eliminar_producto(request, id):
    carrito = Carrito(request)
    producto = Pedido.objects.get(nombreEvento=id)
    carrito.eliminar(producto)
    producto.delete()

    return redirect(to='home')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Pedido.objects.get(nombrePedido=producto_id)
    print(producto)
    carrito.agregar(producto)
    return render(request, 'musica/merchandising.html')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Pedido.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect(to='carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(to='carrito')