"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    
    dicc = {}
    with open("files/input/data.csv", "r") as file:
        data = file.readlines()
        for line in data:
            columns = line.strip().split("\t")
            dict_str = columns[4]
            items = dict_str.split(",")
            for item in items:
                key, value = item.split(":")
                value = int(value)
                key = key.strip()
                if key not in dicc:
                    dicc[key] = [value]
                else:
                    dicc[key].append(value)
    return [(key, min(values), max(values)) for key, values in sorted(dicc.items())]
