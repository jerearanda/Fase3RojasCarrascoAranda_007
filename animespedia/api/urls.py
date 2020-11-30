from django.urls import path

from api.views import AnimesList

app_name = "api"
urlpatterns = [
    path("animes/", AnimesList.as_view(), name="get_animes"),
]
