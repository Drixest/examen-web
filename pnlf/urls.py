from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #Estados
    path('estados', views.ver_estados , name='ver_estados'),
    path('estado/crear/', views.crear_estado, name='crear_estado'),
    path('estado/detalles/<int:estado_id>', views.detalles_estado, name='detalles_estado'),
    path('estado/eliminar/<int:estado_id>', views.eliminar_estado, name='eliminar_estado'),
    path('estado/editar/<int:pk>', views.editar_estado.as_view(), name='editar_estado'),
    #Ciudades
    path('ciudades', views.ver_ciudades , name='ver_ciudades'),
    path('ciudad/crear/', views.crear_ciudad, name='crear_ciudad'),
    path('ciudad/detalles/<int:ciudad_id>', views.detalles_ciudad, name='detalles_ciudad'),
    path('ciudad/eliminar/<int:ciudad_id>', views.eliminar_ciudad, name='eliminar_ciudad'),
    path('ciudad/editar/<int:pk>', views.editar_ciudad.as_view(), name='editar_ciudad'),
    #Estadio
    path('estadios', views.ver_estadios , name='ver_estadios'),
    path('estadio/crear/', views.crear_estadio, name='crear_estadio'),
    path('estadio/detalles/<int:estadio_id>', views.detalles_estadio, name='detalles_estadio'),
    path('estadio/eliminar/<int:estadio_id>', views.eliminar_estadio, name='eliminar_estadio'),
    path('estadio/editar/<int:pk>', views.editar_estadio.as_view(), name='editar_estadio'),
    #Ligas
        path('ligas', views.ver_ligas , name='ver_ligas'),
    path('liga/crear/', views.crear_liga, name='crear_liga'),
    path('liga/detalles/<int:liga_id>', views.detalles_liga, name='detalles_liga'),
    path('liga/eliminar/<int:liga_id>', views.eliminar_liga, name='eliminar_liga'),
    path('liga/editar/<int:pk>', views.editar_liga.as_view(), name='editar_liga'),
    #Equipo
    path('equipos', views.ver_equipos , name='ver_equipos'),
    path('equipo/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipo/detalles/<int:equipo_id>', views.detalles_equipo, name='detalles_equipo'),
    path('equipo/eliminar/<int:equipo_id>', views.eliminar_equipo, name='eliminar_equipo'),
    path('equipo/editar/<int:pk>', views.editar_equipo.as_view(), name='editar_equipo'),
    #Jugadores
    path('jugadores', views.ver_jugadores , name='ver_jugadores'),
    path('jugador/crear/', views.crear_jugador, name='crear_jugador'),
    path('jugador/detalles/<int:jugador_id>', views.detalles_jugador, name='detalles_jugador'),
    path('jugador/eliminar/<int:jugador_id>', views.eliminar_jugador, name='eliminar_jugador'),
    path('jugador/editar/<int:pk>', views.editar_jugador.as_view(), name='editar_jugador'),
]   