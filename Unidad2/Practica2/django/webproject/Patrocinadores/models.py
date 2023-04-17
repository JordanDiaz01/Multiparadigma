from django.db import models
from contratos.models import Contratos
# Create your models here.
class Patrocinadores(models.Model):
    nombre = models.CharField(max_length=255)
    idcontrato = models.ForeignKey(Contratos,on_delete=models.SET_NULL,null=True)
