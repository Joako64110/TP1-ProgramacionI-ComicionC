import random

# Se usaron funciones MUUY simples para hacer los llamados y comodidad

def jere_programa():
    
    '''Este es un programa de piedra papel o tijera contra la maquina'''

    #Funcion, que verifica quien gana y pierde
    def quien_gana(seleccion_random, seleccion_ppt, number):
            # Empate si son iguales
            if number == seleccion_random:
                print(" ")
                print(f"La maquina a elegido: {seleccion_ppt.title()}, y tu: {seleccion_ppt.title()}, Bueno, un simple EMPATE :(")
                print(" ")
            #Los siguiente tres elif, verifican basicamente que el usuario pierda, entonces verifica que el usuario no haya elegido ninguna de las opciones en la que gana
            elif seleccion_random == 1 and number != 3:
                seleccion_random = "piedra"
                print(" ")
                print(f"La maquina a elegido: {seleccion_random.title()}, y tu: {seleccion_ppt.title()}, WAH WAH, HAS PERDIDO!!")
                print(" ")
            elif seleccion_random == 2 and number != 1:
                seleccion_random = "tijera"
                print(" ")
                print(f"La maquina a elegido: {seleccion_random.title()}, y tu: {seleccion_ppt.title()}, WAH WAH, HAS PERDIDO!!")
                print(" ")
            elif seleccion_random == 3 and number != 2:
                seleccion_random = "papel"
                print(" ")
                print(f"La maquina a elegido: {seleccion_random.title()}, y tu: {seleccion_ppt.title()}, WAH WAH, HAS PERDIDO!!")
                print(" ")
            # Con la verificacion anterior, si el usuario elige algo en lo que gana, pasa directamente al else
            else:
                # se podria hacer con directamente el nombre, pero empeze a hacerlo con numeros y quedo
                if seleccion_random == 1:
                    seleccion_random = "piedra"
                elif seleccion_random == 2:
                    seleccion_random = "tijera"
                else:
                    seleccion_random = "papel"
                print(" ")
                print(f"La maquina a elegido: {seleccion_random.title()}, y tu: {seleccion_ppt.title()}, Asique has GANADO!!! FELICIDADES!!!")
                print(" ")
    #Siempre entra al while, y se rompe con el break
    while True:
        # Guardamos en una variable lo que eliga el usuario
        seleccion_ppt = input("Eliga: Piedra, Papel o Tijera o deje el espacio en vacio para salir: ").lower()
        # Verificamos primero que no quiera salir
        if seleccion_ppt == "" or seleccion_ppt == " ":
            print("Gracias por jugar al piedra, papel o tijera, hasta luego :)")
            break
        # Guardamos en una variable lo que elige la maquina con un numero random del 1 al 3
        seleccion_random = random.randint(1,3)
        #Verificamos que se haya pasado una de las tres opciones
        if seleccion_ppt == "piedra" or seleccion_ppt == "tijera" or seleccion_ppt == "papel":
            #Pasamos un numero para los condicionales de la funcion
            if seleccion_ppt == "piedra":
                number = 1
            if seleccion_ppt == "papel":
                number = 3
            if seleccion_ppt == "tijera":
                number = 2
            # Llamamos a la funcion que verifica quien gana.
            quien_gana(seleccion_random, seleccion_ppt, number)
        else:
            print("No a ingresado una opcion correcta")        

#-------------------------------------------------------------------------

def mati_programa():
    while True:
        print("Opciones")                                    #Selecciona las opciones de la calculadora
        print("1: Suma")
        print("2: Resta")
        print("3: Multiplicacion")
        print("4: Division")
        print("5: Salir")
        opt=input("Seleccione la operacion que desea realizar(1/2/3/4/5): ")
        if opt == '5':
            break
        if opt in ("1", "2", "3", "4"):                      #En el caso de seleccionar alguna de las opciones te pide los numeros a calcular
            num_1=float(input("Ingrese el primer numero: "))
            num_2=float(input("Ingrese el segundo numero: "))
            if opt == '1':
                result=num_1+num_2
                print(f"El resultado de la suma entre {num_1} y {num_2} es: {result}")
            elif opt == '2':
                result=num_1-num_2
                print(f"El resultado de la resta entre {num_1} y {num_2} es: {result}")
            elif opt == '3':
                result=num_1*num_2
                print(f"El resultado de la multiplicacion entre {num_1} y {num_2} es: {result}")
        elif opt == '4':
                if num_2 !=0:                                             #Si el segundo numero elegido es 0, no se realiza la operacion.
                    result=num_1/num_2
                    print(f"El resultado de la division entre {num_1} y {num_2} es: {result}")
                else:
                    print("No se puede dividir por cero.")
        else:
            print("Opcion invalida.")

# ----------------------------------------------------------------------


def juan_programa():
    
    '''Este codigo nos permite que ingresando el nombre de alguno de los paises que se muestran como
    opción nos muestre cuando serán los siguientes partidos de su selección de fútbol'''
    print("Paises disponibles: Argentina, Alemania, Japon.")
    pais="a"
    while pais != "":
        pais= input("Ingrese el nombre del pais que desee conocer las fechas o deje un espacio en blanco para finalizar: ").lower()
        if pais == "argentina":
            print("Próximas fecha a jugar:")
            print("Argentina vs Bolivia | 12/09/2023.")
            print("Argentina vs Paraguay | 12/10/2023.")
        elif pais == "alemania":
            print("Próximas fecha a jugar")
            print("Alemania vs Francia | 12/09/2023")
            print("Alemania vs Estados Unidos | 14/10/2023")
        elif pais == "japon":
            print("Próximas fecha a jugar:")
            print("Japón vs Canadá | 13/10/2023.")
            print("Japón vs Túnez | 17/10/2023.")
        elif pais =="":
            break
        else:
            print("El nombre ingresado no corresponde a una opciòn válida")

# ----------------------------------------------------------------------
def joakog_programa():
#Calendario: Éste programa permite guardar una fecha en concreto para recibir una notificación en determinado horario para recordar dicha fecha.

    schedule= {"a": "mañana", "b": "medio día", "c": "tarde", "d": "noche"}
    succes= False

    while succes == False:
        #Se ingresan los datos de la fecha solicitada y se comprueban de que sean datos válidos.
        print("-----<Por favor, ingrese los números correspondientes a cada entrada solicitada, para guardar la fecha que desee>-----")
        month= int(input("Número del mes: "))

        if month > 12 or month < 0:
            print("Mes inexistente. Por favor, reinicie el programa e ingrese el número de un mes válido.")
            continue

        day= int(input("Número del día: "))

        if month == 1:
            if day > 31 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 2:
            if day > 28 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 3:
            if day > 31 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 4:
            if day > 30 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 5:
            if day > 31 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 6:
            if day > 30 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 7:
            if day > 31 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 8:
            if day > 31 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 9:
            if day > 30 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 10:
            if day > 31 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 11:
            if day > 30 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue
        elif month == 12:
            if day > 31 or day < 1:
                print("Día inexistente. Por favor, inténtelo nuevamente e ingrese el número de un día válido. A")
                continue

        year= int(input("Número del año: "))

        if year < 2023:
            print("No es posible almacenar una fecha de un año que ya pasó, por favor inténtelo nuevamente.")
            continue

        #Se establece y se guarda la fecha
        date= f"{day}/{month}/{year}"
        print(f"¡¡Fecha {date} almacenada exitosamente!!")

        #Se solicita la elección del horario en el que desea recibir la notificación y se verífica que el usuario haya ingresado una opción correcta.
        print("¿En qué horario desea recibir la notificación de recordatorio? A= mañana; B= medio día; C= tarde; D= noche")
        choice_sche= input().lower()

        if choice_sche == "a" or choice_sche == "b" or choice_sche == "c" or choice_sche == "d":
            for i in schedule:
                if i == choice_sche:
                    print("Horaio establecido con éxito.")
                    succes= True
                    break
        else:
            print("Opción inválida. Por favor inténtelo de nuevo e ingrese una de las opciones mostradas por pantalla.")
            continue

    print("----------<>Acción realizada con éxito<>----------")

# ----------------------------------------------------------------------
def isma_programa():
        #programa  que busca las posiciones de una subcadena en un texto ingresado

    text = str(input("ingrese un texto:  \n> "))                                            #Pido que ingrese la cadena principal
    phrase = str(input("Ingrese una subcadena desea buscar en el texto anterior: \n> "))  
    number = text.count(phrase)                                                             #averiguo cuantas veces aparece la subcadena en la cadena
    j=0                                     #inicializo la variable en cero
    position_ph = []                               #Creo una lista vacia

    while j < len(text):                    #creo un bucle para encontrar todas las posiciones de la subcadena
        
        if text[j:].find(phrase) == -1:     #En caso de que no encuentre la subcadena saldra del ciclo
            break
        else:                                                               #si encuentra la subcadena agrega su posicion en position_ph
            position_ph.append(text[j:].find(phrase)+len(text[:j]))            
            j = len(text[:j]) + text[j:].find(phrase) + len(phrase) + 1     #La varible j toma el valor de la posicion de la frase encontrada en el texto, y a partir de ahí buscará devuelta la frase en a lcadena principal
            

    print(f"La subcadena '{phrase}' aparece un total de {number} veces en el texto") 
    for index in position_ph:                                   #Imprimo el valor de todas las posiciones en la que se encuentra la frase
        print(f"ubicado en la posicion: {index} \n")

while True:
    print(" ")
    print("Elija a que aplicacion quiere ingresar: ")
    print("1: Calculadora")
    print("2: Piedra, papel o tijera")
    print("3: Fecha Partidos")
    print("4: Calendario")
    print("5: Buscador")
    print("6: Salir")
    print(" ")
    opcion_programa = input("")
    if opcion_programa == "1":
        mati_programa()
    elif opcion_programa == "2":
        jere_programa()
    elif opcion_programa == "3":
        juan_programa()
    elif opcion_programa == "4":
        joakog_programa()
    elif opcion_programa == "5":
        isma_programa()
    elif opcion_programa == "6":
        print("Hasta Luego y buena suerte")
        break
    else:
        print("Opcion incorrecta, por favor, ingresa las opciones que se te proporcionan.")