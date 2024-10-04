# Un serializador convierte los datos del modelo a un formato JSON y viceversa. 
# Crea un archivo serializers.py en la carpeta tareas:

from rest_framework import serializers
from .models import Tarea  # Asegúrate de que este modelo exista

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea  # Indica el modelo que estás serializando
        fields = '__all__'  # O especifica los campos que deseas incluir
