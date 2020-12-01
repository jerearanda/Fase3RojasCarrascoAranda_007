from django.test import TestCase
from animes.models import Anime

class AnimeTestCase(TestCase):

    def setUp(self):
        Anime.objects.create(nombre="Overlord", descripcion="xd overlord uwu", descripcion_corta="Elskwieuryaasdas")  
    def test_anime_descripcion_max_length(self):
        anime1 = Anime.objects.get(id=1)
        max_length = anime1._meta.get_field('descripcion_corta').max_length 
        self.assertEquals(max_length, 500)
    def test_anime_get_absolute_url(self):
        anime1=Anime.objects.get(id=1)
        field_label = anime1._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')    
    def test_nombre_anime(self):
        anime1=Anime.objects.get(id=1)
        self.assertEquals(anime1.nombre, "Overlord")