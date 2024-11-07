from rest_framework.decorators import api_view
from rest_framework.response import Response
from gestion_emploi_du_temps.models import UniteDEnseignement
from .serializers import UniteDEnseignementSerializer

@api_view(['GET', 'POST'])
def uniteDEnseignement_list(request):
    if request.method == 'GET':
        unites = UniteDEnseignement.objects.all()
        serializer = UniteDEnseignementSerializer(unites, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = UniteDEnseignementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Unité d\'enseignement créée avec succès!', 'unite': serializer.data}, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def uniteDEnseignement_detail(request, pk):
    try:
        unite = UniteDEnseignement.objects.get(pk=pk)
    except UniteDEnseignement.DoesNotExist:
        return Response({'error': 'Unité d\'enseignement non trouvée'}, status=404)

    if request.method == 'GET':
        serializer = UniteDEnseignementSerializer(unite)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UniteDEnseignementSerializer(unite, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Unité d\'enseignement mise à jour avec succès!', 'unite': serializer.data})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        unite.delete()
        return Response({'message': 'Unité d\'enseignement supprimée avec succès!'}, status=204)