from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    matricula = models.IntegerField(null=True, blank=True)
    role = models.IntegerField(null=True, blank=True)
    hora_begin = models.TimeField(null=True, blank=True)
    hora_end = models.TimeField(null=True, blank=True)
    horas_except = models.CharField(max_length=255, null=True, blank=True)
    dias_begin = models.IntegerField(null=True, blank=True)
    dias_end = models.IntegerField(null=True, blank=True)
    dias_except = models.IntegerField(null=True, blank=True)
    configurado = models.BooleanField(default=False)

class Materia(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class MateriasProfes(models.Model):
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    profe = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class Asesoria(models.Model):
    profe = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='asesorias_profe')
    estudiante = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='asesorias_estudiante')
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
