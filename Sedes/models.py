from django.db import models

class Sede(models.Model):
    nombre = models.CharField(max_length=100)
    calle = models.CharField(max_length=100)
    altura = models.IntegerField(unique=True)
    
    