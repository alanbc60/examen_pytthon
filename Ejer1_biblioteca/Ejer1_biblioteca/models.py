from django.db import models

# Modelo Autor 

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre


# Libros (título, autor, fecha de publicación) 
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)  # Relación de muchos a uno (un autor puede tener varios libros)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo
