from django.contrib import admin
from . import models

admin.site.register(models.Estado)
admin.site.register(models.Ciudad)
admin.site.register(models.Estadio)
admin.site.register(models.Liga)
admin.site.register(models.Equipo)
admin.site.register(models.Jugador)


