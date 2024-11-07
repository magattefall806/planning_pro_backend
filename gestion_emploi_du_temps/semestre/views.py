from rest_framework.decorators import api_view
from rest_framework.response import Response
from gestion_emploi_du_temps.models import Semestre, Metier
from .serializers import SemestreSerializer, MetierSerializer

@api_view(['GET', 'POST'])
def semestre_list(request, metier_id=None):
    if request.method == 'GET':
        if metier_id:
            semestres = Semestre.objects.filter(metier_id=metier_id)
        else:
            semestres = Semestre.objects.all()
        serializer = SemestreSerializer(semestres, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SemestreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Semestre créé avec succès!', 'semestre': serializer.data}, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def semestre_detail(request, pk):
    try:    
        semestre = Semestre.objects.get(pk=pk)
    except Semestre.DoesNotExist:
        return Response({'error': 'Semestre non trouvé'}, status=404)

    if request.method == 'GET':
        serializer = SemestreSerializer(semestre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SemestreSerializer(semestre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Semestre mis à jour avec succès!', 'semestre': serializer.data})
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        semestre.delete()
        return Response({'message': 'Semestre supprimé avec succès!'}, status=204)