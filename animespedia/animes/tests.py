from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase
from django.urls import reverse

from .views import AnimeDetailView
from .models import Anime


class DetailViewTest(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()

        # Crea un usuario
        self.user = User.objects.create_user(
            username="John", email="john@gmail.com", password="top_secret"
        )

        # Crea un anime
        self.anime = Anime(
            nombre="Overlord",
            descripcion="xd overlord uwu",
            descripcion_corta="Elskwieuryaasdas",
        )
        self.anime.save()

    def test_usuario_registrado_visita_detalle_anime(self):
        # Crea una instacia de una peticion get
        request = self.factory.get(reverse("detalle_anime", args=(self.anime.id,)))

        # necesitas simular un usuario para realizar la petición
        request.user = self.user

        # usar sintaxis vistas basadas en clases
        response = AnimeDetailView.as_view()(request, pk=self.anime.pk)

        self.assertEqual(response.status_code, 200)

    def test_usuario_anonimo_visita_detalle_anime(self):
        # Crea una instacia de una peticion get
        request = self.factory.get(reverse("detalle_anime", args=(self.anime.id,)))

        # Simular un usuario anonimo
        request.user = AnonymousUser()

        # usar sintaxis vistas basadas en clases
        response = AnimeDetailView.as_view()(request, pk=self.anime.pk)

        self.assertEqual(response.status_code, 200)