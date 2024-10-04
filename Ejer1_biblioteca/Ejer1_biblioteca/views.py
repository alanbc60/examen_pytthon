from django.http import HttpResponse

# def hola_django(request):
#     return HttpResponse("Hola, Django!")

from django.shortcuts import render
from .models import Libro
from .models import Autor

def lista_libros(request):
    libros = Libro.objects.all()  # Obtener todos los libros
    return render(request, 'viewLibros.html', {'libros': libros})

 
"""
    Vista que muestra la lista de autores en la plantilla viewAutores.html
    
    Parameters:
    request (HttpRequest): La solicitud HTTP
    
    Returns:
    HttpResponse: La respuesta HTTP con la plantilla viewAutores.html
""" 

def lista_autores(request):
    
    autores = Autor.objects.all()  # Obtener todos los autores
    return render(request, 'viewAutores.html', {'autores': autores})


