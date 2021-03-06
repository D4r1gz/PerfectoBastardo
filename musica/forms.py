from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Evento, Useer, Pedido
class DateTimeInput(forms.DateTimeInput):
    input_type = 'datetime-local'


class EventoForm(ModelForm):
    
    class Meta:
        model = Evento
        fields = ['nombreEvento', 'descripcion', 'fecha', 'precio', 'categoria']
        
    def __init__(self, *args, **kwargs):
        super(EventoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
        })
            self.fields['fecha'].input_formats = ['%d/%m/%Y','%d-%m-%Y']

class UseerForm(forms.Form):

    username = forms.CharField(
        label="Nombre de usuario", widget=forms.TextInput())
    email = forms.EmailField(label="Email", widget=forms.TextInput())
    password_one = forms.CharField(
        label="Password", widget=forms.PasswordInput(render_value=False))
    password_two = forms.CharField(
        label="Confirmar password", widget=forms.PasswordInput(render_value=False))

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            u = User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('El nombre de usuario ya existe')


def clean_email(self):
    email = self.cleaned_data['email']
    try:
        u = User.objects.get(email=email)
    except User.DoesNotExist:
        return email
    raise forms.ValidationError('Email ya registrado')


def clean_password_two(self):
    password_one = self.cleaned_data['password_one']
    password_two = self.cleaned_data['password_two']
    if password_one == password_two:
        pass
    else:
        raise forms.ValidationError('Password no coinciden')

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class productoForm(ModelForm):
    class Meta:
        model: Pedido
        fields=['nombrePedido','stock','precio','imagen']
