from select import select
from django.forms import ModelForm, TextInput , Select
from .models import Estado, Ciudad, Estadio, Liga, Equipo, Jugador

class EstadoForm(ModelForm):
    class Meta:
        model = Estado
        fields = [ 'nombre' ] 
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control mb-2'})
        }

class CiudadForm(ModelForm):
    class Meta:
        model = Ciudad
        fields = [ 'nombre' , 'estado' ] 
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control mb-2'}),
            'estado': Select(attrs={'class': 'form-control mb-2'}),
        }

class EstadioForm(ModelForm):
    class Meta:
        model = Estadio
        fields = [ 'nombre' , 'ciudad' , 'capacidad' ] 
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control mb-2'}),
            'ciudad': Select(attrs={'class': 'form-control mb-2'}),
            'capacidad': TextInput(attrs={'class': 'form-control mb-2', 'type': 'number'})
        }

class LigaForm(ModelForm):
    class Meta:
        model = Liga
        fields = [ 'nombre' ] 
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control mb-2'})
        }

class EquipoForm(ModelForm):
    class Meta:
        model = Equipo
        fields = [ 'nombre' , 'liga' , 'estadio' , 'no_jugadores' ] 
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control mb-2'}),
            'liga': Select(attrs={'class': 'form-control mb-2'}),
            'estadio': Select(attrs={'class': 'form-control mb-2'}),
            'no_jugadores': TextInput(attrs={'class': 'form-control mb-2', 'type': 'number'})
        }

class JugadorForm(ModelForm):
    class Meta:
        model = Jugador
        fields = [ 'nombre' , 'apellido' , 'fecha_nacimiento' , 'equipo' , 'posicion' , 'numero'] 
        widgets = {
            'nombre': TextInput(attrs={'class': 'form-control mb-2'}),
            'apellido': TextInput(attrs={'class': 'form-control mb-2'}),
            'fecha_nacimiento': TextInput(attrs={'class': 'form-control mb-2', 'type': 'date'}),
            'equipo': Select(attrs={'class': 'form-control mb-2'}),
            'numero': TextInput(attrs={'class': 'form-control mb-2', 'type': 'number'}),
            'posicion': TextInput(attrs={'class': 'form-control mb-2'})
        }







