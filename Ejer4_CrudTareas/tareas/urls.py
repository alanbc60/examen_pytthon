from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .api.views import TareaViewSet  # Importa desde la carpeta api

from django.urls import path, include
from .views import index

urlpatterns = [
    path('', index, name='index'),  # Ruta para el index.html
    path('api/', include('tareas.api.urls')),  # Incluir las URLs de la API
]
