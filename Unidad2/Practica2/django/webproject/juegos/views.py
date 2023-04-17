from django.shortcuts import render,redirect,get_object_or_404
from juegos.models import Juego
from juegos.forms import JuegoForm
# Create your views here.

def nuevoJuego(request):
    if request.method == 'POST':
          formaJuego = JuegoForm(request.POST)
          if formaJuego.is_valid():
                formaJuego.save()
                return redirect('indexJuegos')
    else:
            formaJuego= JuegoForm()
    return render(request,'nuevoJuego.html',{'formaJuego': formaJuego})

def editarJuego(req,id):
      juego = get_object_or_404(Juego,pk=id)
      if req.method == 'POST':
        formaJuego = JuegoForm(req.POST,instance=juego)
        if formaJuego.is_valid():
             formaJuego.save()
             return redirect('indexJuegos')
      else:
        formaJuego = JuegoForm(instance=juego)
      return render(req,'editarJuego.html',{'formaJuego': formaJuego})
def eliminarJuego(req,id):
     juego = get_object_or_404(Juego,pk=id)
     if juego:
          juego.delete()
     return redirect('indexJuegos')

def detalleJuego(req,id):
     juego = get_object_or_404(Juego,pk=id)
     return render(req,'detalleJuego.html',{'juego':juego})



