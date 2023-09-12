#--------------------Ejercicio 1--------------------

#Se requiere un programa que muestre por pantalla el incremento de una variable x por ciclo
x = 0
while x <= 30:
    x += 1
    if x == 15:
        break                                   #Concluye el ciclo si el valor de x es igual a 15
    if x ==4 or x==6 or x==10:                  #Cuando la variable tome el valor de 4, 6 o 10 se salteará su impresion por pantalla
        print(f"El valor {x} de x fue omitido")
        continue
    else:
        print(f"El valor del ciclo es:  {x}")

print(f"Se rompió la ejecucuión del bucle cuando x valia: {x}")     	#Muestra el valor final de x una vez termina el ciclo

#--------------------Ejercicio 1--------------------

lines = []
while True:
    line = input("Ingrese una línea de texto (deje en blanco para finalizar): ")
    if not line:
        break
    lines.append(line)

for linea in lines:
    print(linea.upper())

#--------------------Ejercicio 2--------------------

balance = 0
while True:
    operation=input("Ingrese una operación (D para depósito, R para retiro, o línea vacía para salir): ")
    if operation == "":
        break

    if operation == "D":
        amount=int(input("Ingrese el monto a depositar: "))
        if amount < 0:
            print("Ingrese un número mayor a 0")
            continue
        balance += amount
        print("D ",amount)
    elif operation == "R":
        amount=int(input("Ingrese el monto a retirar: "))
        if amount < 0:
            print("Ingrese un número mayor a 0")
            continue
        if amount > balance:
            print("El saldo que quiere retirar es mayor al que posee en la cuenta")
            continue
        balance-= amount
        print("R ",amount)
    else:
        print("Operación no válida")

print ("El saldo de su cuenta es de: ",balance)

#--------------------Ejercicio 3--------------------

cantprim=0

while True:
    num= int(input("Ingrese un numero mayor o igual a 1(0 para salir):"))
    if num==0:
        break
    if num >= 1:
        esPrimo=True
        for i in range(2, num):
            if num % i == 0:
                esPrimo=False
                break
        if esPrimo:
            cantprim+=1
    else:
        print("El numero debe ser mayor o igual que 1")
print(f'La cantidad de numeros primos es: {cantprim}')

#--------------------Ejercicio 4--------------------

first_year = int(input("Ingrese el primer año: "))
second_year = int(input("Ingrese el segundo año: "))
x = range(first_year, second_year+1)
for i in x:
    if i % 10 == 0:
        print(f"El año {i}, es multiplo de 10")
    if i % 4 == 0:
        if i % 100 == 0:
            if i % 400 == 0:
                print(f"El año {i}, es un año biciesto")  
            else:
                print(f"El año {i}, NO es un año biciesto")  
        else:
            print(f"El año {i}, es un año biciesto")

#--------------------Ejercicio 5--------------------

for number in range(1, 21):
    if number % 2 != 0:
        continue
    print(number)

##--------------------Ejercicio 6--------------------

lyst= [1, 12, 23, 34, 45, 56, 67, 78, 89, 901]
t_f= False
number= int(input("Ingrese el número que desee buscar: "))

for i in lyst:
    if i == number:
        print("Se encontró el número ingresado.")
        break

#--------------------Ejercicio 7--------------------

#Se me solicita que con un bucle while pueda elegir multiples opciones y que imprima en cada reiteracion la opción elegida
answer = -1                              #Inicializo la variable en -1
print("Eliga una opción")
print("1-Primera opción \n2-Segunda opción \n3-Tercera opción")
while answer != 0:
    answer = int(input("> "))            #Pido al usuario que eliga una opción
    if answer==0:
        print("\nprograma finalizado")      #Si ingresa cero, finaliza el bucle
        break
    elif answer==1:                      #Si elige una de las opciones, imprimirá la que ha elegido
        print("\nHas elegido la opcion 1")
    elif answer == 2:
        print("\nHas elegido la opcion 2")
    elif answer == 3:
        print("\nHas elegido la opcion 3")
    else:                                           #si no se da ningun un caso, mostrara por pantalla que no ha elegido ninguna opcion
        print("\nNo has elegido ninguna opción") 
    print("\nIngrese otra opción")