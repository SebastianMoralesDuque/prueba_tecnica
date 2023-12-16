from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .serializers import LiderCreateSerializer, CapitanSerializer
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Capitan


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
def registrar_admin(request):
    # Obtener datos del cuerpo de la solicitud
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')

    # Verificar si los datos requeridos se proporcionaron
    if not (username and email and password):
        return Response({'message': 'Se requieren username, email y password'}, status=status.HTTP_400_BAD_REQUEST)

    # Verificar si el username ya existe
    if User.objects.filter(username=username).exists():
        return Response({'message': 'El nombre de usuario ya está en uso'}, status=status.HTTP_400_BAD_REQUEST)

    # Crear el superusuario 'admin'
    admin = User.objects.create_superuser(username, email, password)

    return Response({'message': f'Administrador {username} creado exitosamente'}, status=status.HTTP_201_CREATED)


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

#capitanes
@api_view(['GET'])
def listar_capitanes(request):
    capitanes = Capitan.objects.all()
    serializer = CapitanSerializer(capitanes, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_capitan(request):
    serializer = CapitanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def ver_capitan(request, pk):
    try:
        capitan = Capitan.objects.get(pk=pk)
    except Capitan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CapitanSerializer(capitan)
    return Response(serializer.data)

@api_view(['PUT'])
def actualizar_capitan(request, pk):
    try:
        capitan = Capitan.objects.get(pk=pk)
    except Capitan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CapitanSerializer(capitan, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def eliminar_capitan(request, pk):
    try:
        capitan = Capitan.objects.get(pk=pk)
    except Capitan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    capitan.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)