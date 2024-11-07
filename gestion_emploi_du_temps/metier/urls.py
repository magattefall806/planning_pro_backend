# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from views import MetierViewSet

# router = DefaultRouter()
# router.register(r'metiers', MetierViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]   

from django.urls import path
from . import views

urlpatterns = [
    path('', views.metier_list, name='metier_list'),
    path('<int:pk>/', views.metier_detail, name='metier_detail'),
    path('total/', views.total_metiers, name='total_metiers'),
]