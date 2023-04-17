from django.shortcuts import render,redirect,get_object_or_404
from contratos.models import Contratos
from contratos.forms import ContratoForm
# Create your views here.
def nuevoContrato(request):
    if request.method == 'POST':
          formaContrato = ContratoForm(request.POST)
          if formaContrato.is_valid():
                formaContrato.save()
                return redirect('indexContratos')
    else:
            formaContrato= ContratoForm()
    return render(request,'nuevoContrato.html',{'formaContrato': formaContrato})

def editarContrato(req,id):
      contrato = get_object_or_404(Contratos,pk=id)
      if req.method == 'POST':
        formaContrato = ContratoForm(req.POST,instance=contrato)
        if formaContrato.is_valid():
             formaContrato.save()
             return redirect('indexContratos')
      else:
        formaContrato = ContratoForm(instance=contrato)
      return render(req,'editarContrato.html',{'formaContrato': formaContrato})
def eliminarContrato(req,id):
     contrato = get_object_or_404(Contratos,pk=id)
     if contrato:
          contrato.delete()
     return redirect('indexContratos')

def detalleContrato(req,id):
     contrato = get_object_or_404(Contratos,pk=id)
     return render(req,'detalleContrato.html',{'contrato':contrato})



