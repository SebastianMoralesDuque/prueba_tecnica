from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Departamento, Municipio, Barrio, Comuna, PuestoVotacion
from .serializers import DepartamentoSerializer, MunicipioSerializer, BarrioSerializer, ComunaSerializer, PuestoVotacionSerializer
from rest_framework.permissions import IsAuthenticated



#Departamentos

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def departamento_list(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No tienes permisos para acceder a esta información'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def departamento_detail(request, pk):
    try:
        departamento = Departamento.objects.get(pk=pk)
        serializer = DepartamentoSerializer(departamento)
        return Response(serializer.data)
    except Departamento.DoesNotExist:
        return Response({'error': 'El departamento no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def departamento_create(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        serializer = DepartamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'No tienes permisos para crear un nuevo departamento'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def departamento_update(request, pk):
    try:
        departamento = Departamento.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            serializer = DepartamentoSerializer(departamento, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No tienes permisos para actualizar este departamento'}, status=status.HTTP_403_FORBIDDEN)
    except Departamento.DoesNotExist:
        return Response({'error': 'El departamento no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def departamento_delete(request, pk):
    try:
        departamento = Departamento.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            departamento.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'No tienes permisos para eliminar este departamento'}, status=status.HTTP_403_FORBIDDEN)
    except Departamento.DoesNotExist:
        return Response({'error': 'El departamento no existe'}, status=status.HTTP_404_NOT_FOUND)

#Municipios

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def municipio_list(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        municipios = Municipio.objects.all()
        serializer = MunicipioSerializer(municipios, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No tienes permisos para acceder a esta información'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def municipio_detail(request, pk):
    try:
        municipio = Municipio.objects.get(pk=pk)
        serializer = MunicipioSerializer(municipio)
        return Response(serializer.data)
    except Municipio.DoesNotExist:
        return Response({'error': 'El municipio no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def municipio_create(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        serializer = MunicipioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'No tienes permisos para crear un nuevo municipio'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def municipio_update(request, pk):
    try:
        municipio = Municipio.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            serializer = MunicipioSerializer(municipio, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No tienes permisos para actualizar este municipio'}, status=status.HTTP_403_FORBIDDEN)
    except Municipio.DoesNotExist:
        return Response({'error': 'El municipio no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def municipio_delete(request, pk):
    try:
        municipio = Municipio.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            municipio.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'No tienes permisos para eliminar este municipio'}, status=status.HTTP_403_FORBIDDEN)
    except Municipio.DoesNotExist:
        return Response({'error': 'El municipio no existe'}, status=status.HTTP_404_NOT_FOUND)
    
#Barrios

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def barrio_list(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        barrios = Barrio.objects.all()
        serializer = BarrioSerializer(barrios, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No tienes permisos para acceder a esta información'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def barrio_detail(request, pk):
    try:
        barrio = Barrio.objects.get(pk=pk)
        serializer = BarrioSerializer(barrio)
        return Response(serializer.data)
    except Barrio.DoesNotExist:
        return Response({'error': 'El barrio no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def barrio_create(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        serializer = BarrioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'No tienes permisos para crear un nuevo barrio'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def barrio_update(request, pk):
    try:
        barrio = Barrio.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            serializer = BarrioSerializer(barrio, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No tienes permisos para actualizar este barrio'}, status=status.HTTP_403_FORBIDDEN)
    except Barrio.DoesNotExist:
        return Response({'error': 'El barrio no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def barrio_delete(request, pk):
    try:
        barrio = Barrio.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            barrio.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'No tienes permisos para eliminar este barrio'}, status=status.HTTP_403_FORBIDDEN)
    except Barrio.DoesNotExist:
        return Response({'error': 'El barrio no existe'}, status=status.HTTP_404_NOT_FOUND)
    
#Comunas

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comuna_list(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        comunas = Comuna.objects.all()
        serializer = ComunaSerializer(comunas, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No tienes permisos para acceder a esta información'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def comuna_detail(request, pk):
    try:
        comuna = Comuna.objects.get(pk=pk)
        serializer = ComunaSerializer(comuna)
        return Response(serializer.data)
    except Comuna.DoesNotExist:
        return Response({'error': 'La comuna no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comuna_create(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        serializer = ComunaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'No tienes permisos para crear una nueva comuna'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def comuna_update(request, pk):
    try:
        comuna = Comuna.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            serializer = ComunaSerializer(comuna, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No tienes permisos para actualizar esta comuna'}, status=status.HTTP_403_FORBIDDEN)
    except Comuna.DoesNotExist:
        return Response({'error': 'La comuna no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comuna_delete(request, pk):
    try:
        comuna = Comuna.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            comuna.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'No tienes permisos para eliminar esta comuna'}, status=status.HTTP_403_FORBIDDEN)
    except Comuna.DoesNotExist:
        return Response({'error': 'La comuna no existe'}, status=status.HTTP_404_NOT_FOUND)

#Puestos de votación


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def puesto_list(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        puestos_votacion = PuestoVotacion.objects.all()
        serializer = PuestoVotacionSerializer(puestos_votacion, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'No tienes permisos para acceder a esta información'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def puesto_detail(request, pk):
    try:
        puesto_votacion = PuestoVotacion.objects.get(pk=pk)
        serializer = PuestoVotacionSerializer(puesto_votacion)
        return Response(serializer.data)
    except PuestoVotacion.DoesNotExist:
        return Response({'error': 'El puesto de votación no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def puesto_create(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
        serializer = PuestoVotacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'No tienes permisos para crear un nuevo puesto de votación'}, status=status.HTTP_403_FORBIDDEN)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def puesto_update(request, pk):
    try:
        puesto_votacion = PuestoVotacion.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            serializer = PuestoVotacionSerializer(puesto_votacion, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'No tienes permisos para actualizar este puesto de votación'}, status=status.HTTP_403_FORBIDDEN)
    except PuestoVotacion.DoesNotExist:
        return Response({'error': 'El puesto de votación no existe'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def puesto_delete(request, pk):
    try:
        puesto_votacion = PuestoVotacion.objects.get(pk=pk)
        if hasattr(request.user, 'userprofile') and request.user.userprofile.is_lider:
            puesto_votacion.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({'error': 'No tienes permisos para eliminar este puesto de votación'}, status=status.HTTP_403_FORBIDDEN)
    except PuestoVotacion.DoesNotExist:
        return Response({'error': 'El puesto de votación no existe'}, status=status.HTTP_404_NOT_FOUND)