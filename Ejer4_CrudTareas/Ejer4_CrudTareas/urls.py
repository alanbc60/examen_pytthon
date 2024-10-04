from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('', include('tareas.urls')),  # Rutas de la app tareas
    path('api/', include('tareas.api.urls')),  # Rutas de la API
]
