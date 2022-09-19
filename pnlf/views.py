from tkinter import E
from django.views.generic.edit import UpdateView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Estado,Ciudad,Estadio,Liga,Equipo,Jugador
from .forms import EstadoForm,CiudadForm,EstadioForm,LigaForm,EquipoForm,JugadorForm

def index(request):
    return render(request,'index.html')

#Estados#
def ver_estados(request):
     estados = Estado.objects.order_by('-id')
     return render(request,'estado/index.html', { 'estados': estados })

def detalles_estado(request, estado_id):
    estado = get_object_or_404(Estado, pk=estado_id)
    return render(request, 'estado/detalles.html' , { 'estado': estado })

class editar_estado(UpdateView):
    model = Estado
    form_class = EstadoForm
    template_name = 'estado/editar.html'
    success_url = '/estados'

def eliminar_estado(request, estado_id):
    if request.method == 'POST':
        estado = get_object_or_404(Estado, pk=estado_id)
        estado.delete()
    return redirect(ver_estados)

def crear_estado(request):
    context = {}
    form = EstadoForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = 'Se agrego el estado'
    context['form'] = form
    return render(request, 'estado/crear.html', context)

#Ciudad#

def ver_ciudades(request):
     ciudades = Ciudad.objects.order_by('-id')
     return render(request,'ciudad/index.html', { 'ciudades': ciudades })

def detalles_ciudad(request, ciudad_id):
    ciudad = get_object_or_404(Ciudad, pk=ciudad_id)
    return render(request, 'ciudad/detalles.html' , { 'ciudad': ciudad })

class editar_ciudad(UpdateView):
    model = Ciudad
    form_class = CiudadForm
    template_name = 'ciudad/editar.html'
    success_url = '/ciudad'

def eliminar_ciudad(request, ciudad_id):
    if request.method == 'POST':
        ciudad = get_object_or_404(Ciudad, pk=ciudad_id)
        ciudad.delete()
    return redirect(ver_ciudades)

def crear_ciudad(request):
    context = {}
    form = CiudadForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = 'Se agrego la ciudad'
    context['form'] = form
    return render(request, 'ciudad/crear.html', context)

#Estadio
def ver_estadios(request):
     estadios = Estadio.objects.order_by('-id')
     return render(request,'estadio/index.html', { 'estadios': estadios })

def detalles_estadio(request, estadio_id):
    estadio = get_object_or_404(Estadio, pk=estadio_id)
    return render(request, 'estadio/detalles.html' , { 'estadio': estadio })

class editar_estadio(UpdateView):
    model = Estadio
    form_class = EstadioForm
    template_name = 'estadio/editar.html'
    success_url = '/estadios'

def eliminar_estadio(request, estadio_id):
    if request.method == 'POST':
        estadio = get_object_or_404(Estadio, pk=estadio_id)
        estadio.delete()
    return redirect(ver_estadios)

def crear_estadio(request):
    context = {}
    form = EstadioForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = 'Se agrego el estadio'
    context['form'] = form
    return render(request, 'estadio/crear.html', context)
#Liga
def ver_ligas(request):
     ligas = Liga.objects.order_by('-id')
     return render(request,'liga/index.html', { 'ligas': ligas })

def detalles_liga(request, liga_id):
    liga= get_object_or_404(Liga, pk=liga_id)
    return render(request, 'liga/detalles.html' , { 'liga': liga })

class editar_liga(UpdateView):
    model = Liga
    form_class = LigaForm
    template_name = 'liga/editar.html'
    success_url = '/liga'

def eliminar_liga(request, liga_id):
    if request.method == 'POST':
        liga = get_object_or_404(Liga, pk=liga_id)
        liga.delete()
    return redirect(ver_ligas)

def crear_liga(request):
    context = {}
    form = LigaForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = 'Se agrego la liga'
    context['form'] = form
    return render(request, 'liga/crear.html', context)
#Equipo
def ver_equipos(request):
     equipos = Equipo.objects.order_by('-id')
     return render(request,'equipo/index.html', { 'equipos': equipos })

def detalles_equipo(request, equipo_id):
    equipo= get_object_or_404(Equipo, pk=equipo_id)
    return render(request, 'equipo/detalles.html' , { 'equipo': equipo })

class editar_equipo(UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/editar.html'
    success_url = '/equipo'

def eliminar_equipo(request, equipo_id):
    if request.method == 'POST':
        equipo = get_object_or_404(Equipo, pk=equipo_id)
        equipo.delete()
    return redirect(ver_equipos)

def crear_equipo(request):
    context = {}
    form = EquipoForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = 'Se agrego el equipo'
    context['form'] = form
    return render(request, 'equipo/crear.html', context)
#Jugador
def ver_jugadores(request):
     jugadores = Jugador.objects.order_by('-id')
     return render(request,'jugador/index.html', { 'jugadores': jugadores })

def detalles_jugador(request, jugador_id):
    jugador= get_object_or_404(Jugador, pk=jugador_id)
    return render(request, 'jugador/detalles.html' , { 'jugador': jugador })

class editar_jugador(UpdateView):
    model = Jugador
    form_class = JugadorForm
    template_name = 'jugador/editar.html'
    success_url = '/jugador'

def eliminar_jugador(request, jugador_id):
    if request.method == 'POST':
        jugador = get_object_or_404(jugador, pk=jugador_id)
        jugador.delete()
    return redirect(ver_jugadores)

def crear_jugador(request):
    context = {}
    form = JugadorForm(request.POST or None)
    if form.is_valid():
        form.save()
        context['success'] = 'Se agrego el jugador'
    context['form'] = form
    return render(request, 'jugador/crear.html', context)