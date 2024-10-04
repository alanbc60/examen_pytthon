# Un serializador convierte los datos del modelo a un formato JSON y viceversa. 
# Crea un archivo serializers.py en la carpeta tareas:

from rest_framework import serializers
from .models import Tarea  # Asegúrate de que esté importado correctamente

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ['id', 'nombre', 'descripcion', 'fecha_creacion', 'estado']
