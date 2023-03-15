from django.shortcuts import render
from personas.models import Persona
# Create your views here.

def index(req):
    return render(req,'Bienvenido.html')


def indexPersonas(req):
    noPersonas =  Persona.objects.count()
    personas  =  Persona.objects.order_by('id')
    
    return render(req,'indexPersonas.html',{'noPersonas': noPersonas,'personas': personas })
