from django.shortcuts import render,redirect,get_object_or_404
from Historial.models import Historial
from Historial.forms import HistorialForm
# Create your views here.

def nuevoHistorial(request):
    if request.method == 'POST':
          formaHistorial = HistorialForm(request.POST)
          if formaHistorial.is_valid():
                formaHistorial.save()
                return redirect('indexHistorial')
    else:
            formaHistorial= HistorialForm()
    return render(request,'nuevoHistorial.html',{'formaHistorial': formaHistorial})

def editarHistorial(req,id):
      historial = get_object_or_404(Historial,pk=id)
      if req.method == 'POST':
        formaHistorial = HistorialForm(req.POST,instance=historial)
        if formaHistorial.is_valid():
             formaHistorial.save()
             return redirect('indexHistorial')
      else:
        formaHistorial = HistorialForm(instance=historial)
      return render(req,'editarHistorial.html',{'formaHistorial': formaHistorial})
def eliminarHistorial(req,id):
     historial = get_object_or_404(Historial,pk=id)
     if historial:
          historial.delete()
     return redirect('indexHistorial')

def detalleHistorial(req,id):
     historial = get_object_or_404(Historial,pk=id)
     return render(req,'detalleHistorial.html',{'historial':historial})



