from django.urls import path
from . import views

urlpatterns = [
    path('', views.departement_list, name='departement_list'),
    path('<int:pk>/', views.departement_detail, name='departement_detail'),
]   