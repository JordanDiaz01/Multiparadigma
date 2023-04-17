from django.db import models
from contratos.models import Contratos
# Create your models here.
class Historial(models.Model):
    victorias = models.CharField(max_length=255)
    derrotas = models.CharField(max_length=255)
    fecha = models.CharField(max_length=255)
    idcontrato = models.ForeignKey(Contratos,on_delete=models.SET_NULL,null=True)
