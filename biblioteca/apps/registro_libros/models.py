from django.db import models

# Create your models here.


class Autor(models.Model):
    nombre = models.Charfield(max_length=200)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre
        
    class Meta:
        app_label = 'registro_libros'
        verbose_name_plural = 'Autores(as)'
        
class Libro(models.Model):
    nombre = models.CharField(max_length=200)
    cant_paginas = models.PositiveIntegerField()
    autor = models.ForeignKey(Autor)

    def __str__(self):
        return self.nombre
        
    class Meta:
        app_label = 'registro_libros'
        verbose_name_plural = 'Libros'
