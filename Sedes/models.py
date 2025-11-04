from django.db import models
import uuid

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    altura = models.IntegerField(unique=True)
    codigo = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
    
    