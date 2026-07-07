"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():

    with open("/files/input/data.csv","r") as file:
        data = file.readlines()
        suma = 0
        for line in data:
            columns = line.strip().split("\t")
            suma += int(columns[1])
    return suma

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
