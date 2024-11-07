from django.db import models
from django.http import JsonResponse

class Departement(models.Model):
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    localisation = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'gestion_emploi_du_temps_departement'

    def __str__(self):
        return self.nom

class Metier(models.Model):
    code = models.CharField(max_length=25)
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
        
    class Meta:
        db_table = 'gestion_emploi_du_temps_metier'
        
        
    def __str__(self):
        return self.nom

class Semestre(models.Model):
    numero = models.IntegerField()
    nom = models.CharField(max_length=100)
    date_debut = models.DateField(max_length=25)
    date_fin = models.DateField(max_length=25)
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'gestion_emploi_du_temps_semestre'

    def __str__(self):
        return self.nom
    
class UniteDEnseignement(models.Model):
    nom = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    volume_horaire = models.IntegerField()
    credit = models.IntegerField()
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'gestion_emploi_du_temps_unitedenseignement'
    
    def __str__(self):
        return self.nom
    