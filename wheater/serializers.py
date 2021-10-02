from django.db.models import fields
from rest_framework import serializers
from .models import Wheater

class WheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wheater
        fields = (
            'date',
            'lat',
            'city',
            'state',
            'temperatures',
        )
