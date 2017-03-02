from __future__ import unicode_literals

from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField


# Create your models here.

class Ayudante(models.Model):
	nombres= models.CharField(max_length=50)
	apellidos= models.CharField(max_length=50)
	correo= models.EmailField()
	paralelo= models.IntegerField()
	aula= models.CharField(max_length=50)
	horario= models.CharField(max_length=50)
	def __str__(self):
		return self.nombres + " " + self.apellidos

class AyudanteTareas(models.Model):
	nombres= models.CharField(max_length=50)
	apellidos= models.CharField(max_length=50)
	correo= models.EmailField()
	paralelo= models.IntegerField()
	aula= models.CharField(max_length=50)
	horario= models.CharField(max_length=50)

class Ayudantia(models.Model):
	DIA_CHOICES = (
		("Lunes", 'Lunes'),
		("Martes", 'Martes'),
		("Miercoles", 'Miercoles'),
		("Jueves", 'Jueves'),
		("Viernes", 'Viernes')
		)
	dia = models.CharField(
		max_length=10,
		choices=DIA_CHOICES)
	horaInicio= models.TimeField()
	horaFin= models.TimeField()
	ayudante= models.ForeignKey("Ayudante", null=True)
	aula= models.CharField(max_length=10)
	edificio= models.CharField(max_length=10)
	mapa= models.URLField(max_length=250)

class Profesor(models.Model):
	nombres= models.CharField(max_length=50)
	apellidos= models.CharField(max_length=50)
	correo= models.EmailField()
	paralelo= models.IntegerField()
	oficina= models.CharField(max_length=20)
	coordinador= models.BooleanField()
	img= models.URLField(blank=True)

class Clase(models.Model):
	parcial= models.IntegerField(validators=[MaxValueValidator(2), MinValueValidator(1)])
	semana= models.IntegerField(validators=[MaxValueValidator(7), MinValueValidator(1)])
	clase= models.IntegerField(validators=[MaxValueValidator(2), MinValueValidator(1)])
	tema= models.CharField(max_length=50)
	descripcion= models.CharField(max_length=50)
	video= models.BooleanField()
	linkVideo= models.URLField()
	diapositiva= models.BooleanField()
	linkDiapositiva= models.FileField(blank=True, upload_to='diapositivas/')
	lectura= models.BooleanField()
	linkLectura= models.FileField(blank=True)
	linkCap= models.FileField(blank=True)
	controlLectura= models.BooleanField()
	leccion= models.BooleanField()
	taller= models.BooleanField()
	deber= models.BooleanField()
	proyecto= models.BooleanField()

class Seccion(models.Model):
	DESCRIPCION = 'DES'
	SYLLABUS = 'SYL'
	POLITICAS = 'POL'
	TITULO_CHOICES = (
		(DESCRIPCION, 'Descripcion'),
		(SYLLABUS, 'Syllabus'),
		(POLITICAS, 'Politicas')
		)
	titulo = models.CharField(max_length=3, choices=TITULO_CHOICES, unique=True)
	contenido = RichTextField()
	def __str__(self):
		return self.get_titulo_display()

class Requisito(models.Model):
	codigo= models.CharField(max_length=12, primary_key=True)
	nombre= models.CharField(max_length=50)

class CoRequisito(models.Model):
	codigo= models.CharField(max_length=12, primary_key=True)
	nombre= models.CharField(max_length=50)

class Noticia(models.Model):
	titulo = models.CharField(max_length=100)
	contenido = RichTextField()
	fecha = models.DateField()
	def __str__(self):
		return self.titulo + " " + str(self.fecha)