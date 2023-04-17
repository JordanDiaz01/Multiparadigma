from django.shortcuts import render
from juegos.models import Juego
from contratos.models import Contratos
from Empleados.models import Empleado
from Historial.models import Historial
from Jugadores.models import Jugadores
from Patrocinadores.models import Patrocinadores
# Create your views here.

def index(req):
    return render(req,'bienvenido.html')

def indexJuegos(req):
    noJuegos =  Juego.objects.count()
    juegos  =  Juego.objects.order_by('id')
    
    return render(req,'indexJuegos.html',{'noJuegos': noJuegos,'juegos': juegos })

def indexContratos(req):
    noContratos =  Contratos.objects.count()
    contratos  =  Contratos.objects.order_by('id')
    
    return render(req,'indexContratos.html',{'noContratos': noContratos,'contratos': contratos })

def indexEmpleados(req):
    noEmpleados =  Empleado.objects.count()
    empleados  =  Empleado.objects.order_by('id')
    
    return render(req,'indexEmpleados.html',{'noEmpleados': noEmpleados,'empleados': empleados })

def indexHistorial(req):
    noHistorial =  Historial.objects.count()
    historiales  =  Historial.objects.order_by('id')
    
    return render(req,'indexHistorial.html',{'noHistorial': noHistorial,'historiales': historiales })

def indexJugadores(req):
    noJugadores =  Jugadores.objects.count()
    jugadores  =  Jugadores.objects.order_by('id')
    
    return render(req,'indexJugadores.html',{'noJugadores': noJugadores,'jugadores': jugadores })

def indexPatrocinadores(req):
    noPatrocinadores =  Patrocinadores.objects.count()
    patrocinadores  =  Patrocinadores.objects.order_by('id')
    
    return render(req,'indexPatrocinadores.html',{'noPatrocinadores': noPatrocinadores,'patrocinadores': patrocinadores })
