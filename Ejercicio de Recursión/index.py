#--------------------Ejercicio 1--------------------

import random

def experiment(path, time):
    if path == 1:
        chosen_path= random.randint(1, 3)
        time += 3
        return experiment(chosen_path, time)
    elif path == 2:
        chosen_path= random.randint(1, 3)
        time += 5
        return experiment(chosen_path, time)
    elif path == 3:
        time += 7
        return time

chosen_path= random.randint(1, 3)
time= 0
#print(chosen_path)
print(f"La rata tardó {experiment(chosen_path, time)} minutos en salir de la jaula")

#--------------------Ejercicio 2--------------------

#Consigna apropiada para la función presentada:
'''Crea una función recursiva llamada "f" que toma un número ("n") entero positivo como entrada y devuelve su versión invertida'''