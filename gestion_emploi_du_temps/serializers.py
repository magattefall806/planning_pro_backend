from rest_framework import serializers
from .models import Departement, Metier, Semestre, UniteDEnseignement

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = '__all__'

class MetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metier
        fields = '__all__'

class SemestreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semestre
        fields = '__all__'

class UniteDEnseignementSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniteDEnseignement
        fields = '__all__'