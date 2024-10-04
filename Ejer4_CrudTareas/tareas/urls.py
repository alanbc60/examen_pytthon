from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api.views import TareaViewSet  # Importa desde la carpeta api


router = DefaultRouter()
router.register(r'tareas', TareaViewSet)  # Registra el viewset

urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del router
]
