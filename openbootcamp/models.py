from django.db import models

class Directores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    peliculas = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.nombre + self.apellido + self.peliculas
    
class Pelicula(models.Model):
    director = models.CharField(max_length=50)
    nombre_p = models.CharField(max_length=50)
    sinopsis = models.TextField()
    
    def __str__(self):
        return self.nombre_p
    
    