from django.db import models

class Asociado(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField
    fecha_de_nacimiento = models.DateField(null=True)
    
    def __str__(self):
        return f"Asociado: {self.nombre} {self.apellido}"