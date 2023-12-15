from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from localizaciones.models import Municipio, PuestoVotacion
from .models import Lider, Votante
from .serializers import VotanteSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def registrar_votante(request):
    usuario_registrador = request.user

    try:
        lider_registrador = Lider.objects.get(
            user_profile__user=usuario_registrador)
    except Lider.DoesNotExist:
        return Response({'error': 'No tienes permisos para registrar un votante'}, status=status.HTTP_403_FORBIDDEN)

    votante_data = request.data
    votante_data['lider'] = lider_registrador.id

    serializer = VotanteSerializer(data=votante_data)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Votante registrado correctamente'}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def listar_votantes(request):
    usuario = request.user

    try:
        lider = Lider.objects.get(user_profile__user=usuario)
    except Lider.DoesNotExist:
        return Response({'error': 'No tienes permisos para ver los votantes'}, status=status.HTTP_403_FORBIDDEN)

    votantes = Votante.objects.filter(lider=lider)

    serializer = VotanteSerializer(votantes, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editar_votante(request, pk):
    usuario = request.user

    try:
        lider_registrador = Lider.objects.get(user_profile__user=usuario)
    except Lider.DoesNotExist:
        return Response({'error': 'No tienes permisos para registrar un votante'}, status=status.HTTP_403_FORBIDDEN)

    try:
        lider = Lider.objects.get(user_profile__user=usuario)
    except Lider.DoesNotExist:
        return Response({'error': 'No tienes permisos para editar votantes'}, status=status.HTTP_403_FORBIDDEN)

    try:
        votante = Votante.objects.get(pk=pk)
    except Votante.DoesNotExist:
        return Response({'error': 'El votante que intentas editar no existe'}, status=status.HTTP_404_NOT_FOUND)

    if votante.lider != lider:
        return Response({'error': 'No puedes editar este votante'}, status=status.HTTP_403_FORBIDDEN)

    votante_data = request.data
    votante_data['lider'] = lider_registrador.id

    serializer = VotanteSerializer(votante, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Votante editado correctamente'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_votante(request, pk):
    usuario = request.user

    try:
        lider = Lider.objects.get(user_profile__user=usuario)
    except Lider.DoesNotExist:
        return Response({'error': 'No tienes permisos para eliminar votantes'}, status=status.HTTP_403_FORBIDDEN)

    try:
        votante = Votante.objects.get(pk=pk)
    except Votante.DoesNotExist:
        return Response({'error': 'El votante que intentas eliminar no existe'}, status=status.HTTP_404_NOT_FOUND)

    if votante.lider != lider:
        return Response({'error': 'No puedes eliminar este votante'}, status=status.HTTP_403_FORBIDDEN)

    votante.delete()
    return Response({'message': 'Votante eliminado correctamente'}, status=status.HTTP_204_NO_CONTENT)

# servicios


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cantidad_votantes_lider(request, lider_id):
    try:
        lider = Lider.objects.get(pk=lider_id)
    except Lider.DoesNotExist:
        return JsonResponse({'error': 'El líder no existe'}, status=404)

    cantidad_votantes = Votante.objects.filter(lider=lider).count()

    return JsonResponse({'cantidad_votantes_lider': cantidad_votantes})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cantidad_total_votantes(request):
    cantidad_total = Votante.objects.count()

    return JsonResponse({'cantidad_total_votantes': cantidad_total})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cantidad_votantes_municipio(request, municipio_id):
    try:
        municipio_existente = Municipio.objects.filter(
            id_municipio=municipio_id).exists()
        if not municipio_existente:
            return JsonResponse({'error': 'El municipio no existe'}, status=404)

        cantidad_votantes = Votante.objects.filter(puesto_votacion__comuna__barrio__municipio_id=municipio_id) \
            .count()
        return JsonResponse({'cantidad_votantes_municipio': cantidad_votantes})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cantidad_votantes_mesa(request, mesa_id):
    try:
        mesa_existente = PuestoVotacion.objects.filter(
            id_puesto_votacion=mesa_id).exists()
        if not mesa_existente:
            return JsonResponse({'error': 'La mesa de votación no existe'}, status=404)

        cantidad_votantes = Votante.objects.filter(
            puesto_votacion_id=mesa_id).count()
        return JsonResponse({'cantidad_votantes_mesa': cantidad_votantes})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
