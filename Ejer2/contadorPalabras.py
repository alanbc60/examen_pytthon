# Escribe un script en Python que lea un archivo de texto y cuente la cantidad de palabras que contiene.

# ejecucion:  python3 contadorPalabras.py

import os


def verificadorArchivo(archivo):
    # Obtener la extensión del archivo
    _, extension = os.path.splitext(archivo)
    
    # Lista de extensiones permitidas
    extensiones_validas = ['.txt', '.md', '.csv', '.log'] 
    
    # Comprobar si la extensión es válida
    return extension.lower() in extensiones_validas



"""
    Abre un archivo de texto y devuelve la cantidad de palabras que contiene.

    Parametros:
        nombre_archivo (str): nombre del archivo de texto.

    Retorna:
        int: cantidad de palabras del archivo.
"""



def contar_palabras(archivo):

    if not verificadorArchivo(archivo):
        print("El archivo no es un archivo de texto.")
        return 0

    try:
        # abrir archivo en modo lectura
        with open(archivo, 'r') as archivo:

            # leer el archivo
            texto = archivo.read()

            # dividir el texto en palabras
            palabras = texto.split()
            return len(palabras)
    except FileNotFoundError:
        print("El archivo no existe o no se pudo abrir.")
        return 0
    
# Uso
# print(contar_palabras('archivo.txt'))


if __name__ == "__main__":
    totalPalabras = contar_palabras('textoPrueba.txt')
    if totalPalabras > 0:
        print("El archivo tiene", totalPalabras, "palabras.")
    else:
        print("El archivo no tiene palabras.")

