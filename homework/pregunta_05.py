"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():


    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    dicc = {}
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
        for line in data:
            columns = line.strip().split("\t")
            letter = columns[0]
            num = int(columns[1])
            if letter not in dicc:
                dicc[letter] = [num]
            else:
                dicc[letter].append(num)
    return [(letter, max(values), min(values)) for letter, values in sorted(dicc.items())]