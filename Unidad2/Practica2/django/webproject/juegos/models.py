from django.db import models

# Create your models here.
class Juego(models.Model):
    nombrejuego = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    compañia = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Juego {self.nombrejuego} {self.genero} {self.compañia}'


