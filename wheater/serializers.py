from django.db.models import fields
from rest_framework import serializers
from .models import Wheater

class WheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheater
        fields = (
            'id',
            'date',
            'lat',
            'lon',
            'city',
            'state',
            'temperatures',
        )
