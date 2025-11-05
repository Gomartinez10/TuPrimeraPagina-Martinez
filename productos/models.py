from django.db import models
import uuid

class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField(null=True, blank=True)
    imagen = models.ImageField(
        upload_to='articulos/',  
        null=True,
        blank=True,
        help_text="Sube una imagen del artículo"
    )
    
    codigo = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    def __str__(self):
        return f"{self.nombre} ({self.codigo})"
    