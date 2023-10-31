#Inicializo listas de pasajeros y ciudades
lista_pasajeros = []
lista_ciudades = []

#Función para agregar pasajeros a la lista de viajeros
def agregar_pasajero():
    nombre = input("Nombre del pasajero: ")
    dni = int(input("DNI del pasajero: "))
    destino = input("Ciudad de destino: ")
    lista_pasajeros.append((nombre, dni, destino))
    print("Pasajero agregado exitosamente.")

#Función para agregar ciudades a la lista de ciudades
def agregar_ciudad():
    ciudad = input("Nombre de la ciudad: ")
    pais = input("País al que pertenece: ")
    lista_ciudades.append((ciudad, pais))
    print("Ciudad agregada exitosamente.")

#Función para buscar la ciudad de destino de un pasajero por DNI
def buscar_ciudad_por_dni():
    dni = int(input("DNI del pasajero: "))
    for pasajero in lista_pasajeros:
        if pasajero[1] == dni:
            destino = pasajero[2]
            print(f"El pasajero con DNI {dni} viaja a {destino}.")
            return
    print(f"No se encontró un pasajero con DNI {dni}.")

#Función para mostrar la cantidad de pasajeros que viajan a una ciudad
def contar_pasajeros_por_ciudad():
    ciudad = input("Ciudad: ")
    count = sum(1 for pasajero in lista_pasajeros if pasajero[2] == ciudad)
    print(f"La cantidad de pasajeros que viajan a {ciudad} es {count}.")

#Función para buscar el país de destino de un pasajero por DNI
def buscar_pais_por_dni():
    dni = int(input("DNI del pasajero: "))
    for pasajero in lista_pasajeros:
        if pasajero[1] == dni:
            destino = pasajero[2]
            for ciudad, pais in lista_ciudades:
                if ciudad == destino:
                    print(f"El pasajero con DNI {dni} viaja a {destino}, en el país {pais}.")
                    return
    print(f"No se encontró un pasajero con DNI {dni}.")

#Función para mostrar la cantidad de pasajeros que viajan a un país
def contar_pasajeros_por_pais():
    pais = input("País: ")
    count = sum(1 for pasajero in lista_pasajeros for ciudad, p in lista_ciudades if ciudad == pasajero[2] and p == pais)
    print(f"La cantidad de pasajeros que viajan a {pais} es {count}.")

#Menú iterativo
while True:
    print("\n--- Menú ---")
    print("1. Agregar pasajero")
    print("2. Agregar ciudad")
    print("3. Ver ciudad por DNI")
    print("4. Ver cantidad de pasajeros por ciudad")
    print("5. Ver país por DNI")
    print("6. Ver cantidad de pasajeros por país")
    print("7. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        agregar_pasajero()
    elif opcion == '2':
        agregar_ciudad()
    elif opcion == '3':
        buscar_ciudad_por_dni()
    elif opcion == '4':
        contar_pasajeros_por_ciudad()
    elif opcion == '5':
        buscar_pais_por_dni()
    elif opcion == '6':
        contar_pasajeros_por_pais()
    elif opcion == '7':
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, elija una opción válida.")
