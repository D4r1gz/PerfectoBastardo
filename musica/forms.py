from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Evento, Useer
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

class UseerForm( ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
