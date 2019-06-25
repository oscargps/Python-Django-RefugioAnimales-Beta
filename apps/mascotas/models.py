from django.db import models
from apps.adopcion.models import Persona

class Vacuna(models.Model):
    nombre=models.CharField(max_length=20)
    def __str__(self):
        return '{}'.format(self.nombre)
class Mascota(models.Model):
    nombre=models.CharField(max_length=50)
    raza=models.CharField(max_length=10)
    sexo=models.CharField(max_length=10)
    edad=models.IntegerField()
    fecha_rescue=models.DateField()
    persona=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna=models.ManyToManyField(Vacuna, blank=True)

