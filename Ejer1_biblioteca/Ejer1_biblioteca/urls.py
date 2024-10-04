from django.urls import path
from .views import lista_autores, lista_libros

urlpatterns = [
    path('autores/', lista_autores, name='lista_autores'),
    path('libros/', lista_libros, name='lista_libros'),
]
