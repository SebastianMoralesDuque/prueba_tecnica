from rest_framework import serializers
from .models import Departamento, Municipio, Barrio, Comuna, PuestoVotacion


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class BarrioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrio
        fields = '__all__'


class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'


class PuestoVotacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuestoVotacion
        fields = '__all__'
