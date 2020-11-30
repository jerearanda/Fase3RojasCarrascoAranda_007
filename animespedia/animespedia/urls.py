"""animespedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from animes.views import *
from django.conf import settings
from django.conf.urls.static import static



###############
## URLs de admin ##generos
###############
urlpatterns = [
    path('admin/', admin.site.urls),
    path ('animes/', include('animes.urls')),
    path('api/', include('api.urls')),
]

###############
## URLs de anime ##
###############

urlpatterns += [
    path ("", AnimeListView.as_view(), name="inicio"),
    path ("animes/<int:pk>/", AnimeDetailView.as_view(), name="detalle_anime"),
    path ("animes/<int:pk>/delete", AnimeDelete.as_view(), name="borrar_anime"),
    path ("animes/create", AnimeCreate.as_view(), name="crear_anime"),
    path ("animes/<int:pk>/update", AnimeUpdate.as_view(), name="editar_anime"),
    path("", include("accounts.urls")),
]

###############
## URLs de autor ##
###############
urlpatterns += [
    path ("autores/", AutorListView.as_view(), name="lista_autores"),
    path ("autores/<int:pk>/", AutorDetailView.as_view(), name="detalle_autor"),
    path ("autores/<int:pk>/delete", AutorDelete.as_view(), name="borrar_autor"),
    path ("autores/create", AutorCreate.as_view(), name="crear_autor"),
    path ("autores/<int:pk>/update", AutorUpdate.as_view(), name="editar_autor"),
]

###############
## URLs de paginas#
###############

urlpatterns += [
    path ("inicio_anime/", inicio_anime, name="inicio_anime"),
    path ("galeria_snk/", galeria_snk, name="galeria_snk"),
    path ("personajes_snk/", personajes_snk, name="personajes_snk"),
    path ("formulario_snk/", formulario_snk, name="formulario_snk"),
    path ("inicio_snk_real/", inicio_snk_real, name="inicio_snk_real"),

    path ("inicio_storm/", inicio_storm, name="inicio_storm"),
    path ("galeria_storm/", galeria_storm, name="galeria_storm"),
    path ("personajes_storm/", personajes_storm, name="personajes_storm"),
    path ("test_storm/", test_storm, name="test_storm"),

    path ("inicio_op/", inicio_op, name="inicio_op"),
    path ("personajes_op/", personajes_op, name="personajes_op"),
    path ("galeria_op/", galeria_op, name="galeria_op"),
    path ("test_op/", test_op, name="test_op"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

###############
## URLs de AnimeGen ##
###############
urlpatterns += [
    path ("generos/", AnimeGenListView.as_view(), name="lista_generos"),
    path ("generos/<int:pk>/", AnimeGenDetailView.as_view(), name="detalle_genero"),
    path ("generos/<int:pk>/delete", AnimeGenDelete.as_view(), name="borrar_genero"),
    path ("generos/create", AnimeGenCreate.as_view(), name="crear_genero"),
    path ("generos/<int:pk>/update", AnimeGenUpdate.as_view(), name="editar_genero"),
]
