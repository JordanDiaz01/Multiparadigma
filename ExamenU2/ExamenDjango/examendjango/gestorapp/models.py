from django.db import models

# Create your models here.
class Escuela(models.Model):
    nombreEscuela = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Escuela {self.nombreEscuela} {self.ciudad} {self.telefono} '
    
class Domicilio(models.Model):
    calle = models.CharField(max_length=255)
    colonia= models.CharField(max_length=255)
    NoDepartamento =  models.CharField(max_length=255)
    def __str__(self) -> str:
        return f'Domicilio {self.calle} {self.colonia} {self.NoDepartamento}'
    
class Gerentes(models.Model):
    nombre =  models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    puesto =  models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete = models.SET_NULL, null = True)
    escuela = models.ForeignKey(Escuela, on_delete = models.SET_NULL, null = True)
    def __str__(self) -> str:
        return f'Gerente {self.nombre} {self.apellido} {self.puesto} {self.domicilio} {self.escuela}'

class Estudiante(models.Model):
    nombre =  models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    domicilio = models.ForeignKey(Domicilio, on_delete = models.SET_NULL, null = True)
    escuela = models.ForeignKey(Escuela, on_delete = models.SET_NULL, null = True)
    def __str__(self) -> str:
        return f'Estudiante {self.nombre} {self.apellido} {self.domicilio} {self.escuela}'
    
class Maestro(models.Model):
     nombre =  models.CharField(max_length=255)
     apellido = models.CharField(max_length=255)
     carrera  = models.CharField(max_length=255)
     domicilio = models.ForeignKey(Domicilio, on_delete = models.SET_NULL, null = True)
     escuela = models.ForeignKey(Escuela, on_delete = models.SET_NULL, null = True)
     def __str__(self) -> str:
        return f'Maestro {self.nombre} {self.apellido} {self.carrera} {self.domicilio} {self.escuela}'