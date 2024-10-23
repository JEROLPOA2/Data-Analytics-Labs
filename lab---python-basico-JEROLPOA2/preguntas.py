"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    with open("data.csv", "r") as data:
        
        numbers = [int(col[2]) for col in data]

        return sum(numbers)
    

def pregunta_02():


    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """

    with open("data.csv", "r") as data:

        letters = [col[0] for col in data]
        
        dic = {}

        for i in letters:

            if i not in dic: 
                dic[i] = 1
            
            else:
                dic[i] += 1
        
        dic = list(dic.items())
    
        return list(sorted(dic))



def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    with open("data.csv", "r") as data:

        letters_numbers = [(col[0], int(col[2])) for col in data]
        
        dic = {}

        for i, j in letters_numbers:

            if i not in dic: 
                dic[i] = j
            
            else:
                dic[i] += j
        
        dic = list(dic.items())
    
        return list(sorted(dic))

    

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open("data.csv", "r") as data:

        dates = [col.split("\t")[2] for col in data]
        
        months = [x.split("-")[1] for x in dates]
        
        dic = {}

        for i in months:

            if i not in dic: 
                dic[i] = 1
            
            else:
                dic[i] += 1
        
        dic = list(dic.items())
    
        return list(sorted(dic))
    

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open("data.csv", "r") as data:

        letters_numbers = [(col[0], int(col[2])) for col in data]
        letters_numbers = list(sorted(letters_numbers))

        sublist = {}

        for letter, number in letters_numbers:
            
            if letter not in sublist:
                sublist[letter] = [number]
            
            else:
                sublist[letter].append(number)
          
        sublist = list(sublist.items())
        maxmin = []

        for elem in sublist:
            maxmin.append((elem[0], elem[1][-1], elem[1][0]))

        return maxmin


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    with open("data.csv", "r") as data:

        keys = [col.split()[4] for col in data]
        keys = [x.split(",") for x in keys]

        dic = {}

        for i in keys:

            for j in i:

                key, value = j.split(":")

                if key not in dic:
                    dic[key] = [int(value)]
                
                else:
                    dic[key].append(int(value))
        
        dic = list(dic.items())
        dic = [list(x) for x in dic]
        
        for i in dic:
            i[1] = sorted(i[1])
        
        maxmin = []

        for elem in dic:
            maxmin.append((elem[0], elem[1][0], elem[1][-1]))
        
        return list(sorted(maxmin))
    

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    with open("data.csv", "r") as data:

        letters_numbers = [(col[0], int(col[2])) for col in data]

        dic = {}

        for letter, number in letters_numbers:
            
            if number not in dic:
                dic[number] = [letter]
            
            else:
                dic[number].append(letter)


        dic = list(dic.items())
        return list(sorted(dic))
        

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """

    with open("data.csv", "r") as data:

        letters_numbers = [(col[0], int(col[2])) for col in data]

        dic = {}

        for letter, number in letters_numbers:
            
            if number not in dic:
                dic[number] = [letter]
            
            else:
                dic[number].append(letter)

        dic = list(dic.items())
        dic = [list(x) for x in dic]

        for i in dic:
            
            i[1] = list(sorted(set(i[1])))
        
        dic = list(sorted([tuple(x) for x in dic]))
        
        return dic


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    with open("data.csv", "r") as data:

        keys = [col.split()[4] for col in data]
        keys = [x.split(",") for x in keys]
        keys = [x for sublist in keys for x in sublist]
        keys = list(sorted(keys))

        dic = {}

        for i in keys:
            
            key, value = i.split(":")

            if key not in dic:
                dic[key] = 1
                
            else:
                dic[key] += 1

        return dic 
    

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open("data.csv", "r") as data:
        
        entries = [col.split() for col in data]
        entries = [(x[0], len(x[3].split(",")), len(x[4].split(","))) for x in entries]
        
        return entries
        


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }

    """
    with open("data.csv", "r") as data:

        entries = [col.split() for col in data]
        entries = [[x[3].split(","), int(x[1])] for x in entries]

        dic = {}

        for li in entries:

            for i in li[0]:

                if i not in dic:
                    dic[i] = li[1]
                
                else:
                    dic[i] += li[1]
        
        dic = dict(sorted(dic.items()))
        return dic


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    with open("data.csv", "r") as data:

        entries = [col.split() for col in data]
        entries = [
            [x[0], 
             sum([int(s) for s in x[4].replace(",", " ").replace(":", " ").split() if s.isdigit()])
            ] 
            for x in entries]

        dic = {}

        for key, value in entries:

            if key not in dic:
                dic[key] = value
                
            else:
                dic[key] += value
        
        dic = dict(sorted(dic.items()))
        return dic

