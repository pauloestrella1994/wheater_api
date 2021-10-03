from rest_framework import serializers
from rest_framework import generics
from .models import Wheater
from .serializers import WheaterSerializer


class WheatersView(generics.ListCreateAPIView):
    serializer_class = WheaterSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city', None)
        date = self.request.query_params.get('date', None)
        sort = self.request.query_params.get('sort', None)
        queryset = Wheater.objects.all()

        if city:
            data = city.split(",")
            queryset = queryset.filter(city__in=data)

        if date:
            queryset = queryset.filter(date=date)
        
        if sort:
            queryset = queryset.filter().order_by(sort)
        
        return queryset
        

class WheaterView(generics.RetrieveAPIView):
    queryset = Wheater.objects.all()
    serializer_class = WheaterSerializer