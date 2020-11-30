from rest_framework import serializers
from animes.models import Anime

class AnimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['nombre', 'descripcion', 'autor', 'genero', 'descripcion_corta', 'imagen_portada', 'imagen_fondo', 'imagen_logo', 'imagen_descripcion']
