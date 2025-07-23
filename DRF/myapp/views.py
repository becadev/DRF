from django.shortcuts import render
from rest_framework import generics
from .models import Music
from .serializers import MusicSerializer

# generic class based view
# generics.ListCreateAPIView: imprementa get e post 
class MusicListView(generics.ListCreateAPIView):
    queryset = Music.objects.all() 
    serializer_class = MusicSerializer
