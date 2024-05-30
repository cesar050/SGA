from django.core.validators import MinLengthValidator
from django.db import models


class Facultad(models.Model):
    nombre = models.CharField(max_length=100,
                              unique=True,
                              help_text='Nombre de la facultad',
                              validators=[MinLengthValidator(3)])
    siglas = models.CharField(max_length=10,
                              blank=True,
                              help_text='Siglas de la facultad')
    def __str__(self):
        return self.nombre


class Modalidad(models.Choices):
    PRESENCIAL = 'Presencial'
    SEMIPRESENCIAL = 'Semipresencial'
    DISTANCIA = 'Distancia'


class Carrera(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    facultad = models.ForeignKey(Facultad,
                                 on_delete=models.CASCADE,
                                 related_name='carrerasList')
    modalidad = models.CharField(max_length=20,
                                    choices=Modalidad.choices,
                                    default=Modalidad.PRESENCIAL)

    def __str__(self):
        return self.nombre


class Ciclo(models.Model):
    numero = models.PositiveIntegerField()
    carrera = models.ForeignKey(Carrera,
                                on_delete=models.CASCADE,
                                related_name='ciclosList')

    def __str__(self):
        return f'{self.numero} - {self.carrera.nombre}'


class Asignatura(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    aa = models.CharField(max_length=10)
    acd = models.CharField(max_length=10)
    ape = models.CharField(max_length=10)
    ciclo = models.ForeignKey(Ciclo,
                              on_delete=models.CASCADE,
                              related_name='asignaturasList')

    def __str__(self):
        return self.nombre
