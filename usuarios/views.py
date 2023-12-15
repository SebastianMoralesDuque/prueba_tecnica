from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import LiderCreateSerializer
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import LiderCreateSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registrar_lider(request):

    if not request.user.is_superuser:
        return Response({'error': 'No estás autorizado para realizar esta acción'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'POST':
        username = request.data.get('username', None)
        if username and User.objects.filter(username=username).exists():
            return Response({'error': 'Ya existe un líder con ese nombre de usuario'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = LiderCreateSerializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            lider = serializer.save()
            return Response({'message': 'Líder registrado correctamente', 'lider_id': lider.id}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
def lider_login(request):
    if request.method == 'POST':
        username = request.data.get('username', '')
        password = request.data.get('password', '')

        user = authenticate(username=username, password=password)
        print(user)
        if user:
            if user.userprofile.is_lider:
                login(request, user)

                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=200)
            else:
                return Response({'error': 'Usuario no es líder'}, status=403)
        else:
            return Response({'error': 'Credenciales inválidas'}, status=401)

    return Response({'error': 'Método no permitido'}, status=405)
