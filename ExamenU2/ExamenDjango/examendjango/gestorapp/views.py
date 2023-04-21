from django.shortcuts import render,redirect,get_object_or_404
from gestorapp.models import Estudiante
from gestorapp.forms import EstudianteForm
# Create your views here.

def nuevoEstudiante(request):
    if request.method == 'POST':
          formaEstudiante = EstudianteForm(request.POST)
          if formaEstudiante.is_valid():
                formaEstudiante.save()
                return redirect('indexEstudiante')
    else:
            formaEstudiante= EstudianteForm()
    return render(request,'nuevoEstudiante.html',{'formaEstudiante': formaEstudiante})

def editarEstudiante(req,id):
      estudiante = get_object_or_404(Estudiante,pk=id)
      if req.method == 'POST':
        formaEstudiante = EstudianteForm(req.POST,instance=estudiante)
        if formaEstudiante.is_valid():
             formaEstudiante.save()
             return redirect('indexEstudiante')
      else:
        formaEstudiante = EstudianteForm(instance=estudiante)
      return render(req,'editarEstudiante.html',{'formaEstudiante': formaEstudiante})
def eliminarEstudiante(req,id):
     estudiante = get_object_or_404(Estudiante,pk=id)
     if estudiante:
          estudiante.delete()
     return redirect('indexEstudiante')

def detalleEstudiante(req,id):
     estudiante = get_object_or_404(Estudiante,pk=id)
     return render(req,'detalleEstudiante.html',{'estudiante':estudiante})





