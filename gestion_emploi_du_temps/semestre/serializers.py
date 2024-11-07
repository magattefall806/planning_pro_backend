from rest_framework import serializers
from gestion_emploi_du_temps.models import Semestre, Metier
from gestion_emploi_du_temps.metier.serializers import MetierSerializer

class SemestreSerializer(serializers.ModelSerializer):
    metier = serializers.PrimaryKeyRelatedField(queryset=Metier.objects.all())
    
    class Meta:
        model = Semestre
        fields = ['id', 'numero','nom', 'date_debut', 'date_fin', 'metier']
    
    
    