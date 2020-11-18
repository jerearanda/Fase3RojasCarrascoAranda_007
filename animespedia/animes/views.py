from django.shortcuts import render

# Vistas basadas en clases
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

# Modelos
from animes.models import Anime

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
    fields = ['nombre', 'descripcion', 'descripcion_corta'] #al agregar un nuevo model cambiar esto
    success_url = reverse_lazy('inicio')
#Vista de Editar
class AnimeUpdate(UpdateView):
    model = Anime
    fields = ['nombre', 'descripcion', 'descripcion_corta']
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