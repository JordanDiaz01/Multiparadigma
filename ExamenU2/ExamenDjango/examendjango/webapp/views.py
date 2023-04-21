from django.shortcuts import render
from gestorapp.models import *
# Create your views here.
def index(req):
    return render(req,'index.html')

def indexDomicilio(req):
    noDomicilios =  Domicilio.objects.count()
    domicilios  =  Domicilio.objects.order_by('id')
    
    return render(req,'indexDomicilio.html',{'noDomicilios': noDomicilios,'domicilios': domicilios })

def indexEscuela(req):
    noEscuelas =  Escuela.objects.count()
    escuelas  =  Escuela.objects.order_by('id')
    
    return render(req,'indexEscuela.html',{'noEscuelas': noEscuelas,'escuelas': escuelas })

def indexEstudiante(req):
    noEstudiantes =  Estudiante.objects.count()
    estudiantes  =  Estudiante.objects.order_by('id')
    
    return render(req,'indexEstudiante.html',{'noEstudiantes': noEstudiantes,'estudiantes': estudiantes })

def indexGerente(req):
    noGerentes =  Gerentes.objects.count()
    gerentes  =  Gerentes.objects.order_by('id')
    
    return render(req,'indexGerente.html',{'noGerentes': noGerentes,'gerentes': gerentes })

def indexMaestro(req):
    noMaestros =  Maestro.objects.count()
    maestros  =  Maestro.objects.order_by('id')
    
    return render(req,'indexMaestro.html',{'noMaestros': noMaestros,'maestros': maestros })