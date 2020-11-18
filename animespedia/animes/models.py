from django.db import models
from django.urls import reverse

class Autor(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	nacimiento = models.DateField()

class AnimeGen(models.Model):
	"""Model representing an author."""
	name = models.CharField(max_length=100)
	summary = models.TextField(max_length=1000)

	class Meta:
		ordering = ['name']

	#def get_absolute_url(self):
		#return reverse('genre-detail', args=[str(self.id)]) #entrega la url del recurso

	def __str__(self):
		"""String for representing the Model object."""
		return self.name

class Anime(models.Model):
	nombre=models.CharField(max_length=100)
	descripcion = models.TextField()
	descripcion_corta = models.TextField(max_length=500)
	autor=models.ForeignKey(Autor,on_delete= models.CASCADE, blank=True, null=True)
	genero=models.ForeignKey(AnimeGen,on_delete= models.CASCADE, blank=True, null=True)

	def __str__(self):
 		return self.nombre

