from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TareaViewSet  # Importa tu viewset

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)  # Registra el viewset

urlpatterns = [
    path('', include(router.urls)),  # Incluir las rutas del router
]
