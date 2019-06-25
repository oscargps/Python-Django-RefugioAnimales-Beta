from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=50)
    telefono=models.CharField(max_length=12)
    edad=models.IntegerField()
    direccion=models.TextField()
    mail=models.EmailField()

    def __str__(self):
        return '{}'.format(self.nombre)


class Solicitud(models.Model):
	persona= models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	numero_mascotas= models.IntegerField()
	razones=models.TextField()
		
