import re
from rest_framework import serializers
from .models import Votante


class VotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votante
        fields = '__all__'

    def validate_cedula(self, value):
        cedula_valida = re.match(r'^\d{10}$', value)
        if not cedula_valida:
            raise serializers.ValidationError(
                "La cédula debe tener un formato válido para Colombia (10 dígitos).")

        votante_instance = getattr(self, 'instance', None)

        if votante_instance and votante_instance.pk:
            cedula_existente = Votante.objects.exclude(
                pk=votante_instance.pk).filter(cedula=value).exists()
        else:
            cedula_existente = Votante.objects.filter(cedula=value).exists()

        if cedula_existente:
            raise serializers.ValidationError(
                "Esta cédula ya ha sido registrada.")

        return value

    def validate_telefono(self, value):
        telefono_valido = re.match(r'^\d{10}$', value)
        if not telefono_valido:
            raise serializers.ValidationError(
                "El número de teléfono debe tener exactamente 10 dígitos.")

        return value

    def validate_nombres(self, value):
        if not all(char.isalpha() or char.isspace() for char in value):
            raise serializers.ValidationError(
                "El campo 'nombres' solo puede contener letras y espacios.")
        return value

    def validate_apellidos(self, value):
        if not all(char.isalpha() or char.isspace() for char in value):
            raise serializers.ValidationError(
                "El campo 'apellidos' solo puede contener letras y espacios.")
        return value
