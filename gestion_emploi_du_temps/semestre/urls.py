# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from views import SemestreViewSet

# router = DefaultRouter()
# router.register(r'semestres', SemestreViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.semestre_list, name='semestre_list'),
    path('<int:metier_id>/', views.semestre_list, name='semestre_list'),
    path('<int:pk>/', views.semestre_detail, name='semestre_detail'),
]