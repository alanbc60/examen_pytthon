from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from ..models import Tarea  # Asegúrate de tener un modelo llamado Tarea
from ..serializers import TareaSerializer  # Asegúrate de tener un serializador

# ViewSet para manejar las tareas
class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()  # Obtiene todas las tareas
    serializer_class = TareaSerializer  # Serializador que se utilizará para la API

    def create(self, request, *args, **kwargs):
        print(request.data)  # Depuración
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)  # Depuración
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        # Si necesitas manejar un método adicional (por ejemplo, para validaciones)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
