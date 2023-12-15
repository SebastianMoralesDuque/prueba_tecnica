from rest_framework import serializers
from .models import Votante

class VotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votante
        fields = '__all__'
