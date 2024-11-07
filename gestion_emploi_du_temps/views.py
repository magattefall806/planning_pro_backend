from rest_framework import viewsets
from .models import Departement, Metier, Semestre, UniteDEnseignement
from .serializers import DepartementSerializer, MetierSerializer, SemestreSerializer, UniteDEnseignementSerializer


class DepartementViewSet(viewsets.ModelViewSet):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer

class MetierViewSet(viewsets.ModelViewSet):
    queryset = Metier.objects.all()
    serializer_class = MetierSerializer

class SemestreViewSet(viewsets.ModelViewSet):
    queryset = Semestre.objects.all()
    serializer_class = SemestreSerializer

class UniteDEnseignementViewSet(viewsets.ModelViewSet):
    queryset = UniteDEnseignement.objects.all()
    serializer_class = UniteDEnseignementSerializer