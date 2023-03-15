from django.shortcuts import render,redirect,get_object_or_404
from personas.models import Persona
from personas.forms import PersonaForm
# Create your views here.

def nuevaPersona(request):
    if request.method == 'POST':
          formaPersona = PersonaForm(request.POST)
          if formaPersona.is_valid():
                formaPersona.save()
                return redirect('indexPersonas')
    else:
            formaPersona= PersonaForm()
    return render(request,'nuevo.html',{'formaPersona': formaPersona})

def editarPersona(req,id):
      persona = get_object_or_404(Persona,pk=id)
      if req.method == 'POST':
        formaPersona = PersonaForm(req.POST,instance=persona)
        if formaPersona.is_valid():
             formaPersona.save()
             return redirect('indexPersona')
      else:
        formaPersona = PersonaForm(instance=persona)
      return render(req,'editar.html',{'formaPersona': formaPersona})