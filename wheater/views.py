from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Wheater
from .serializers import WheaterSerializer


class WheaterView(APIView):
    def get(self, request):
        wheater = Wheater.objects.all()
        serializer = WheaterSerializer(wheater, many=True)
        return Response(serializer.data)

