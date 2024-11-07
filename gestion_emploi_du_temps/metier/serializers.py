from rest_framework import serializers
from gestion_emploi_du_temps.models import Metier
from gestion_emploi_du_temps.departement.serializers import DepartementSerializer

class MetierSerializer(serializers.ModelSerializer):
    departement = DepartementSerializer
    
    class Meta:
        model = Metier
        fields = ['id', 'code', 'nom', 'description', 'departement']
        
       