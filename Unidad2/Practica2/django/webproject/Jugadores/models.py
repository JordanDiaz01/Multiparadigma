from django.db import models
from contratos.models import Contratos
from juegos.models import Juego
# Create your models here.
class Jugadores(models.Model):
    nombre= models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email =models.CharField(max_length=255)
    idcontrato = models.ForeignKey(Contratos,on_delete=models.SET_NULL,null=True)
    nombrejuego = models.ForeignKey(Juego,on_delete=models.SET_NULL,null=True)
    def __str__(self) -> str:
        return f'Jugador {self.nombre} {self.apellido} {self.email}'
