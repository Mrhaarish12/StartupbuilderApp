from rest_framework import serializers
from .models import Promotionfmodel

class Promotionfserialize(serializers.ModelSerializer):
    class Meta:
        model=Promotionfmodel
        fields="__all__"