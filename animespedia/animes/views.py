from django.shortcuts import render

# Vistas basadas en clases
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Modelos
from animes.models import Anime, Autor, AnimeGen

###################
# Vistas de Anime ######
###################

# Vista de lista
class AnimeListView(ListView):

    model = Anime
    paginate_by = 10  # if pagination is desired

# Vista de detalle
class AnimeDetailView(DetailView):

    model = Anime
#Vista de Eliminar
class AnimeDelete(DeleteView):
    model = Anime
    success_url = reverse_lazy('inicio')

#Vista de Crear
class AnimeCreate(CreateView):
    model = Anime
    fields = ['nombre', 'descripcion', 'autor', 'genero', 'descripcion_corta', 'imagen_portada', 'imagen_fondo', 'imagen_logo', 'imagen_descripcion'] #al agregar un nuevo model cambiar esto
    success_url = reverse_lazy('inicio')

#Vista de Editar
class AnimeUpdate(UpdateView):
    model = Anime
    fields = ['nombre', 'descripcion', 'autor', 'genero', 'descripcion_corta', 'imagen_portada', 'imagen_fondo', 'imagen_logo', 'imagen_descripcion']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('inicio')



def inicio_anime (request):
    return render(request, "animes/base_inicio_anime.html")
def galeria_snk (request):
    return render(request, "animes/base_galeria_snk.html")
def personajes_snk (request):
    return render(request, "animes/base_personajes_snk.html")
def formulario_snk (request):
    return render(request, "animes/base_formulario_snk.html")
def inicio_snk_real (request):
    return render(request, "animes/base_inicio_snk_real.html")
def inicio_storm (request):
    return render(request, "animes/base_inicio_storm.html")
def galeria_storm (request):
    return render(request, "animes/base_galeria_storm.html")
def personajes_storm (request):
    return render(request, "animes/base_personajes_storm.html")
def test_storm (request):
    return render(request, "animes/base_test_storm.html")
def inicio_op (request):
    return render(request, "animes/base_inicio_op.html")
def personajes_op (request):
    return render(request, "animes/base_personajes_op.html")
def galeria_op (request):
    return render(request, "animes/base_galeria_op.html")
def test_op (request):
    return render(request, "animes/base_test_op.html")


###################
# Vistas de Autor ######
###################

# Vista de lista
class AutorListView(ListView):

    model = Autor
    paginate_by = 10  # if pagination is desired

# Vista de detalle
class AutorDetailView(DetailView):

    model = Autor
#Vista de Eliminar
class AutorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('inicio')

#Vista de Crear
class AutorCreate(CreateView):
    model = Autor
    fields = ['nombre', 'apellido', 'nacimiento'] #al agregar un nuevo model cambiar esto
    success_url = reverse_lazy('inicio')

#Vista de Editar
class AutorUpdate(UpdateView):
    model = Autor
    fields = ['nombre', 'apellido', 'nacimiento']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('inicio')

###################
# Vistas de Genero ######
###################

# Vista de lista
class AnimeGenListView(ListView):

    model = AnimeGen
    paginate_by = 10  # if pagination is desired

# Vista de detalle
class AnimeGenDetailView(DetailView):

    model = AnimeGen
#Vista de Eliminar
class AnimeGenDelete(DeleteView):
    model = AnimeGen
    success_url = reverse_lazy('inicio')

#Vista de Crear
class AnimeGenCreate(CreateView):
    model = AnimeGen
    fields = ['name', 'summary'] #al agregar un nuevo model cambiar esto
    success_url = reverse_lazy('inicio')

#Vista de Editar
class AnimeGenUpdate(UpdateView):
    model = Autor
    fields = ['name', 'summary']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('inicio')


