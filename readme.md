


#Ejercicio 3

pip install mysql-connector-python



# Ejercicio4

1. Configuración del Proyecto
Primero, crea un nuevo proyecto de Django y una nueva aplicación:
django-admin startproject Ejer4_CrudTareas

cd Ejer4_crudTareas  # Cambia al directorio del proyecto
python manage.py startapp tareas  # Crea la aplicación llamada "tareas"


instalar el Rest framework
pip install djangorestframework


Después de definir el modelo, no olvides crear y aplicar las migraciones:
python manage.py makemigrations tareas

Aplicar Migraciones: Para aplicar las migraciones a la base de datos, ejecutas el siguiente comando:
python manage.py migrate