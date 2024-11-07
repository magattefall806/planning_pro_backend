from django.urls import path
from . import views

urlpatterns = [
    path('', views.uniteDEnseignement_list, name='uniteDEnseignement_list'),
    path('<int:pk>/', views.uniteDEnseignement_detail, name='uniteDEnseignement_detail'),
]