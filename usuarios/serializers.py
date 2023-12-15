from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Capitan, UserProfile, Lider


class LiderCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    nombres = serializers.CharField(max_length=100)
    apellidos = serializers.CharField(max_length=100)
    ciudad = serializers.CharField(max_length=100)
    direccion = serializers.CharField(max_length=255)
    foto_perfil = serializers.CharField(max_length=255)
    password = serializers.CharField(
        max_length=128, write_only=True)

    def create(self, validated_data):
        request = self.context.get('request')
        superusuario = request.user if request else None

        if superusuario:
            user = User.objects.create(username=validated_data['username'])
            user.set_password(validated_data['password'])
            user.save()

            user_profile = UserProfile.objects.create(user=user, is_lider=True)

            lider = Lider.objects.create(
                user_profile=user_profile,
                superusuario=superusuario,
                nombres=validated_data['nombres'],
                apellidos=validated_data['apellidos'],
                ciudad=validated_data['ciudad'],
                direccion=validated_data['direccion'],
                foto_perfil=validated_data['foto_perfil'],
            )
            return lider
        else:
            raise serializers.ValidationError(
                "No se puede crear el líder sin un superusuario.")


class CapitanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capitan
        fields = '__all__'
