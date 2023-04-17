from django.shortcuts import render,redirect,get_object_or_404
from Jugadores.models import Jugadores
from Jugadores.forms import JugadorForm
# Create your views here.

def nuevoJugador(request):
    if request.method == 'POST':
          formaJugador = JugadorForm(request.POST)
          if formaJugador.is_valid():
                formaJugador.save()
                return redirect('indexJugadores')
    else:
            formaJugador= JugadorForm()
    return render(request,'nuevoJugadores.html',{'formaJugador': formaJugador})

def editarJugador(req,id):
      jugador = get_object_or_404(Jugadores,pk=id)
      if req.method == 'POST':
        formaJugador = JugadorForm(req.POST,instance=jugador)
        if formaJugador.is_valid():
             formaJugador.save()
             return redirect('indexJugadores')
      else:
        formaJugador = JugadorForm(instance=jugador)
      return render(req,'editarJugadores.html',{'formaJugador': formaJugador})
def eliminarJugador(req,id):
     jugador = get_object_or_404(Jugadores,pk=id)
     if jugador:
          jugador.delete()
     return redirect('indexJugadores')

def detalleJugador(req,id):
     jugador = get_object_or_404(Jugadores,pk=id)
     return render(req,'detalleJugadores.html',{'jugador':jugador})



