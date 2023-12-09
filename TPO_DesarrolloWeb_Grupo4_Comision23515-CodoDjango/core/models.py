from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido")
    dni = models.IntegerField(unique=True, verbose_name="DNI")
    email = models.EmailField(max_length=50, unique=True, verbose_name="Email")
    telefono = models.CharField(max_length=50, verbose_name="Telefono")
    create = models.DateField(auto_now_add=True, verbose_name="Fecha de registro")

    class Meta:
        db_table = "alumnos"
        verbose_name = "alumno"
        verbose_name_plural = "alumnos"
        ordering = ["apellido", "nombre"]

    def __str__(self):
        return self.apellido + " " + self.nombre
