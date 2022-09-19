from statistics import mode
from tkinter import CASCADE
from django.db import models

class Estado(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Estadio(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    ciudad = models.ForeignKey(Ciudad,on_delete=models.CASCADE)
    capacidad = models.IntegerField()
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Liga(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    liga = models.ForeignKey(Liga,on_delete=models.CASCADE)
    estadio = models.ForeignKey(Estadio,on_delete=models.CASCADE)
    no_jugadores = models.IntegerField()
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre

class Jugador(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    fecha_nacimiento = models.DateField()
    numero = models.IntegerField()
    equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    posicion = models.CharField(max_length=30)
    creado_el = models.DateTimeField(auto_now_add=True)
    modificado_el = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre
