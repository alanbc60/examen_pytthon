from rest_framework import viewsets
from ..models import Tarea  # Asegúrate de tener un modelo llamado Tarea
from ..serializers import TareaSerializer  # Asegúrate de tener un serializador

# ViewSet para manejar las tareas
class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()  # Obtiene todas las tareas
    serializer_class = TareaSerializer  # Serializador que se utilizará para la API
