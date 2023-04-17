from django.db import models

# Create your models here.
class Contratos(models.Model):
    inicio_contrato = models.CharField(max_length=255)
    terminacion_contrato = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Contrato desde {self.inicio_contrato} hasta {self.terminacion_contrato}'