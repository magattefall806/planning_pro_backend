from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/departement/', include('gestion_emploi_du_temps.departement.urls')),
    path('api/metier/', include('gestion_emploi_du_temps.metier.urls')),
    path('api/semestre/', include('gestion_emploi_du_temps.semestre.urls')),
    path('api/unite_d_enseignement/', include('gestion_emploi_du_temps.uniteDEnseignement.urls')),
]