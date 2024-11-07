from rest_framework import serializers
from gestion_emploi_du_temps.models import Departement

class DepartementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departement
        fields = ['id', 'nom', 'description', 'localisation']