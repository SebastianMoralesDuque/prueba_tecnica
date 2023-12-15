from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Votante
from .serializers import VotanteSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Lider

from django.contrib.auth.models import User
from django.contrib.auth.models import User
from .models import Lider

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registrar_votante(request):
    # Verifica que el usuario autenticado sea un líder
    usuario_registrador = request.user

    try:
        lider_registrador = Lider.objects.get(user_profile__user=usuario_registrador)
    except Lider.DoesNotExist:
        return Response({'error': 'No tienes permisos para registrar un votante'}, status=status.HTTP_403_FORBIDDEN)
    
    serializer = VotanteSerializer(data=request.data)
    
    if serializer.is_valid():
        # Guarda el votante registrado y asigna la instancia de Lider al campo 'lider'
        serializer.save(lider=lider_registrador)
        return Response({'message': 'Votante registrado correctamente'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
