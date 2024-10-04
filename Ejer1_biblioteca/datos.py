import os
import django
from datetime import date

# Configuración del entorno Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ejer1_biblioteca.settings')  # Cambia por el nombre de tu proyecto
django.setup()

# Importar los modelos
from Ejer1_biblioteca.models import Autor, Libro

def main():
    # Autores
    autor1 = Autor(nombre="Gabriel García Márquez", fecha_nacimiento=date(1927, 3, 6))
    autor1.save()

    autor2 = Autor(nombre="Jorge Luis Borges", fecha_nacimiento=date(1899, 6, 24))
    autor2.save()

    autor3 = Autor(nombre="J. K. Rowling", fecha_nacimiento=date(1965, 7, 31))
    autor3.save()

    # Crear un libro asociado al autor
    libro1 = Libro(titulo="Cien años de soledad", autor=autor1, fecha_publicacion=date(1967, 5, 30))
    libro1.save()

    libro2 = Libro(titulo="Harry Potter y la piedra filosofal", autor=autor2, fecha_publicacion=date(1997, 6, 26))
    libro2.save()

    libro3 = Libro(titulo="Harry Potter y la camara de los secretos", autor=autor2, fecha_publicacion=date(1998, 7, 8))
    libro3.save()

    # Imprimir los autores y libros
    # print(f"Autor 1: {autor1}")
    # print(f"Autor 2: {autor2}")
    # print(f"Autor 3: {autor3}")

    # print(f"Libro 1: {libro1}")
    # print(f"Libro 2: {libro2}")
    # print(f"Libro 3: {libro3}")



if __name__ == "__main__":
    main()
