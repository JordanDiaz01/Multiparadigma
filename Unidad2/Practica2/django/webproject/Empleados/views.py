from django.shortcuts import render,redirect,get_object_or_404
from Empleados.models import Empleado
from Empleados.forms import EmpleadoForm
# Create your views here.

def nuevoEmpleado(request):
    if request.method == 'POST':
          formaEmpleado = EmpleadoForm(request.POST)
          if formaEmpleado.is_valid():
                formaEmpleado.save()
                return redirect('indexEmpleados')
    else:
            formaEmpleado= EmpleadoForm()
    return render(request,'nuevoEmpleado.html',{'formaEmpleado': formaEmpleado})

def editarEmpleado(req,id):
      empleado = get_object_or_404(Empleado,pk=id)
      if req.method == 'POST':
        formaEmpleado = EmpleadoForm(req.POST,instance=empleado)
        if formaEmpleado.is_valid():
             formaEmpleado.save()
             return redirect('indexEmpleados')
      else:
        formaEmpleado = EmpleadoForm(instance=empleado)
      return render(req,'editarEmpleado.html',{'formaEmpleado': formaEmpleado})
def eliminarEmpleado(req,id):
     empleado = get_object_or_404(Empleado,pk=id)
     if empleado:
          empleado.delete()
     return redirect('indexEmpleados')

def detalleEmpleado(req,id):
     empleado = get_object_or_404(Empleado,pk=id)
     return render(req,'detalleEmpleado.html',{'empleado':empleado})



