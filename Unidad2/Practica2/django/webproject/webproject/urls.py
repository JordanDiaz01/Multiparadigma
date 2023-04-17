"""
URL configuration for webproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import *
from juegos.views import *
from contratos.views import *
from Empleados.views import *
from Historial.views import * 
from Jugadores.views import *
from Patrocinadores.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),

    path('indexJuegos',indexJuegos, name='indexJuegos'),
    path('nuevoJuego',nuevoJuego),
    path('editarJuego/<int:id>',editarJuego),
    path('eliminarJuego/<int:id>',eliminarJuego),
    path('detalleJuego/<int:id>',detalleJuego),

    path('indexContratos',indexContratos, name='indexContratos'),
    path('nuevoContrato',nuevoContrato),
    path('editarContrato/<int:id>',editarContrato),
    path('eliminarContrato/<int:id>',eliminarContrato),
    path('detalleContrato/<int:id>',detalleContrato),

    path('indexJugadores',indexJugadores, name='indexJugadores'),
    path('nuevoJugadores',nuevoJugador),
    path('editarJugadores/<int:id>',editarJugador),
    path('eliminarJugadores/<int:id>',eliminarJugador),
    path('detalleJugadores/<int:id>',detalleJugador),

    path('indexEmpleados',indexEmpleados, name='indexEmpleados'),
    path('nuevoEmpleado',nuevoEmpleado),
    path('editarEmpleado/<int:id>',editarEmpleado),
    path('eliminarEmpleado/<int:id>',eliminarEmpleado),
    path('detalleEmpleado/<int:id>',detalleEmpleado),

    path('indexPatrocinadores',indexPatrocinadores, name='indexPatrocinadores'),
    path('nuevoPatrocinador',nuevoPatrocinador),
    path('editarPatrocinador/<int:id>',editarPatrocinador),
    path('eliminarPatrocinador/<int:id>',eliminarPatrocinador),
    path('detallePatrocinador/<int:id>',detallePatrocinador),

    path('indexHistorial',indexHistorial, name='indexHistorial'),
    path('nuevoHistorial',nuevoHistorial),
    path('editarHistorial/<int:id>',editarHistorial),
    path('eliminarHistorial/<int:id>',eliminarHistorial),
    path('detalleHistorial/<int:id>',detalleHistorial),
]
