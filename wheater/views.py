from rest_framework import serializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import Wheater
from .serializers import WheaterSerializer


class WheatersView(generics.ListCreateAPIView):
    queryset = Wheater.objects.all()
    serializer_class = WheaterSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'date']

class WheaterView(generics.RetrieveAPIView):
    queryset = Wheater.objects.all()
    serializer_class = WheaterSerializer