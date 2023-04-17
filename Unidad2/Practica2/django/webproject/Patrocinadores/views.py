from django.shortcuts import render,redirect,get_object_or_404
from  Patrocinadores.models import Patrocinadores
from Patrocinadores.forms import PatrocinadorForm
# Create your views here.

def nuevoPatrocinador(request):
    if request.method == 'POST':
          formaPatrocinador = PatrocinadorForm(request.POST)
          if formaPatrocinador.is_valid():
                formaPatrocinador.save()
                return redirect('indexPatrocinadores')
    else:
            formaPatrocinador= PatrocinadorForm()
    return render(request,'nuevoPatrocinador.html',{'formaPatrocinador': formaPatrocinador})

def editarPatrocinador(req,id):
      patrocinador = get_object_or_404(Patrocinadores,pk=id)
      if req.method == 'POST':
        formaPatrocinador = PatrocinadorForm(req.POST,instance=patrocinador)
        if formaPatrocinador.is_valid():
             formaPatrocinador.save()
             return redirect('indexPatrocinadores')
      else:
        formaPatrocinador = PatrocinadorForm(instance=patrocinador)
      return render(req,'editarPatrocinador.html',{'formaPatrocinador': formaPatrocinador})
def eliminarPatrocinador(req,id):
     patrocinador = get_object_or_404(Patrocinadores,pk=id)
     if patrocinador:
          patrocinador.delete()
     return redirect('indexPatrocinadores')

def detallePatrocinador(req,id):
     patrocinador = get_object_or_404(Patrocinadores,pk=id)
     return render(req,'detallePatrocinador.html',{'patrocinador':patrocinador})



