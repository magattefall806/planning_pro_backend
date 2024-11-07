from rest_framework.decorators import api_view
from rest_framework.response import Response
from gestion_emploi_du_temps.models import Departement
from .serializers import DepartementSerializer

@api_view(['GET', 'POST'])
def departement_list(request):
    if request.method == 'GET':
        departements = Departement.objects.all()
        serializer = DepartementSerializer(departements, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = DepartementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Département créé avec succès!',
                'departement': serializer.data
            }, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def departement_detail(request, pk):
    try:
        departement = Departement.objects.get(pk=pk)
    except Departement.DoesNotExist:
        return Response({'error': 'Département non trouvé'}, status=404)

    if request.method == 'GET':
        serializer = DepartementSerializer(departement)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DepartementSerializer(departement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'Département mis à jour avec succès!',
                'departement': serializer.data
            })
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        departement.delete()
        return Response({'message': 'Département supprimé avec succès!'}, status=200)