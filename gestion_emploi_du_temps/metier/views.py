from rest_framework.decorators import api_view
from rest_framework.response import Response
from gestion_emploi_du_temps.models import Metier
from .serializers import MetierSerializer
from gestion_emploi_du_temps.models import Metier
from django.http import JsonResponse
from rest_framework import status


@api_view(['GET', 'POST'])
def metier_list(request):
    if request.method == 'GET':
        metiers = Metier.objects.all()
        serializer = MetierSerializer(metiers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = MetierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Métier créé avec succès!', 'metier': serializer.data}, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def metier_detail(request, pk):
    try:
        metier = Metier.objects.get(pk=pk)
    except Metier.DoesNotExist:
        return Response({'error': 'Métier non trouvé'}, status=404)

    if request.method == 'GET':
        serializer = MetierSerializer(metier)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MetierSerializer(metier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Métier mis à jour avec succès!', 'metier': serializer.data})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        metier.delete()
        return Response({'message': 'Métier supprimé avec succès!'}, status=204)


def total_metiers(request):
    count = Metier.objects.count()
    return JsonResponse({'total_metiers': count})

@api_view(['GET'])
def get_metier_details(request, id):
    try:
        metier = Metier.objects.get(id=id)
        serializer = MetierSerializer(metier)
        return Response(serializer.data)
    except Metier.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

