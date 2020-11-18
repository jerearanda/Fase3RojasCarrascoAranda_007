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
from django.urls import path
from django.urls import include
from animes.views import (AnimeListView, AnimeDetailView, AnimeDelete,AnimeCreate,AnimeUpdate, inicio_anime ,galeria_snk ,personajes_snk, formulario_snk, inicio_snk_real,inicio_storm
,galeria_storm, personajes_storm, test_storm, inicio_op, personajes_op, galeria_op, test_op)

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('animes/', include('animes.urls')),

    path ("", AnimeListView.as_view(), name="inicio"),
    path ("animes/<int:pk>/", AnimeDetailView.as_view(), name="detalle_anime"),
    path ("animes/<int:pk>/delete", AnimeDelete.as_view(), name="borrar_anime"),
    path ("animes/create", AnimeCreate.as_view(), name="crear_anime"),
    path ("animes/<int:pk>/update", AnimeUpdate.as_view(), name="editar_anime"),
]

urlpatterns += [
    path('admin/', admin.site.urls),
    path ('animes/', include('animes.urls')),

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
]
