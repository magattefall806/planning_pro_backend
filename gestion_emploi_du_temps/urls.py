from django.urls import path, include

urlpatterns = [
    path('departement/', include('gestion_emploi_du_temps.departement.urls')),
    path('metier/', include('gestion_emploi_du_temps.metier.urls')),
    path('semestre/', include('gestion_emploi_du_temps.semestre.urls')),
    path('uniteDEnseignement/', include('gestion_emploi_du_temps.uniteDEnseignement.urls')),
]