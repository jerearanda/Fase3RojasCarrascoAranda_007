from animes.models import Anime
from api.serializers import AnimesSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AnimesList(APIView):
    """
    List all animes
    """
    def get(self, request, format=None):
        Animes = Anime.objects.all()
        serializer = AnimesSerializer(Animes, many=True)
        return Response(serializer.data)


