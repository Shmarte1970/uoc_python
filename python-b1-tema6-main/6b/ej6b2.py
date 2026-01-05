"""
Enunciado:
Utilizando un depurador de código para Python. Corrije el error de la
función llamada 'average_of_even_numbers(numbers)' que acepta una lista de
números enteros como entrada y calcula el promedio de todos los números pares
en la lista.

Para depurar el código se puede usar pdb o herramientas de depuración
externas.

La función debe devolver un número flotante redondeado a dos decimales. Si no
hay números pares en la lista, la función debe devolver 0.

Parámetros:
    numbers: una lista de números enteros.

Ejemplo:
    Entrada:
        numbers = [2, 3, 4, 5, 6]
    Salida:
        4.0


Enunciat:
Utilitzant un depurador de codi per a Python. Corregiu l'error de la
funció anomenada 'average_of_even_numbers(numbers)' que accepta una llista de
nombres enters com a entrada i calcula la mitjana de tots els números parells
a la llista.

Per depurar el codi es pot fer servir pdb o eines de depuració
externes.

La funció ha de tornar un nombre flotant arrodonit a dos decimals. Si no
hi ha números parells a la llista, la funció ha de tornar 0.

Paràmetres:
     numbers: una llista de nombres enters.

Exemple:
     Entrada:
         numbers = [2, 3, 4, 5, 6]
     Sortida:
     4.0

"""


from typing import List

    
def average_of_even_numbers(numbers):
    total = 0
    count = 0

    for num in numbers:
        if num % 2 == 0:
            total += num
            count += 1

    if count == 0:
        return 0.0

    average = total / count
    return round(average, 2)


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# numbers = [2, 3, 4, 5, 6]
# result = average_of_even_numbers(numbers)
# print(result)
