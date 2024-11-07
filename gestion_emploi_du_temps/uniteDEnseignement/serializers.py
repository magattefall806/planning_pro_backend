from rest_framework import serializers
from gestion_emploi_du_temps.models import UniteDEnseignement
from gestion_emploi_du_temps.semestre.serializers import SemestreSerializer

class UniteDEnseignementSerializer(serializers.ModelSerializer):
    Semestre = SemestreSerializer
    
    class Meta:
        model = UniteDEnseignement
        fields = ['id', 'nom', 'code', 'volume_horaire', 'credit', 'semestre']
        