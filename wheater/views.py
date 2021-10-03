from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Wheater
from .serializers import WheaterSerializer


class WheaterView(APIView):

    def get(self, request):
        wheater = Wheater.objects.all()
        serializer = WheaterSerializer(wheater, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = WheaterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)