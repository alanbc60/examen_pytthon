# Escribe una función en Python que reciba una lista de números y devuelva una nueva lista con los números ordenados 
# de menor a mayor.


import random 

"""
    Genera una lista de números aleatorios entre inicio y fin.

    Parametros
    ----------
    tam : int  --> Tamaño de la lista a generar.
    inicio : int --> Límite inferior del rango de números a generar.
    fin : int --> Límite superior del rango de números a generar.

    Retorna
    -------
    list --> Nueva lista con los números aleatorios generados.
"""

# def lista_aleatoria(tam, inicio, fin):
#     return [random.randint(inicio, fin) for _ in range(tam)]

"""
    Ordena una lista de n números de menor a mayor.

    Parametros
    ----------
    listaNumeros : list
        Lista de n números a ordenar.

    Retorna
    -------
    list --> Nueva lista con los n meros ordenados de menor a mayor.
"""
def listaNumeros(listaNumeros):

    numerosOrdenados = sorted(listaNumeros)
    return numerosOrdenados

# llamar a la funcion main
if __name__ == "__main__":

    # generar lista aleatoria

    numeros = random.sample(range(0, 100), 10)
    print("Lista aleatoria: " + str(numeros))
    print(listaNumeros(numeros))