#Inicialización del diccionario de socios con los fundadores
socios = {
    1: {'nombre': 'Amanda Núñez', 'ingreso': '17/03/2009', 'cuota_al_dia': True},
    2: {'nombre': 'Bárbara Molina', 'ingreso': '17/03/2009', 'cuota_al_dia': True},
    3: {'nombre': 'Lautaro Campos', 'ingreso': '17/03/2009', 'cuota_al_dia': True}
}

#Función para mostrar la cantidad de socios
def mostrar_cantidad_socios(socios):
    print(f"La cantidad de socios es: {len(socios)}")

#Función para marcar que un socio ha pagado todas las cuotas adeudadas
def pagar_cuotas(socios, numero_socio):
    if numero_socio in socios:
        socios[numero_socio]['cuota_al_dia'] = True
        print(f"El socio {numero_socio} ha pagado todas las cuotas adeudadas.")
    else:
        print(f"No se encontró al socio {numero_socio}.")

#Función para modificar la fecha de ingreso de socios
def modificar_fecha_ingreso(socios, fecha_antigua, fecha_nueva):
    for numero_socio, datos_socio in socios.items():
        if datos_socio['ingreso'] == fecha_antigua:
            datos_socio['ingreso'] = fecha_nueva

#Función para dar de baja a un socio
def dar_de_baja(socios, nombre_apellido):
    for numero_socio, datos_socio in socios.copy().items():
        if datos_socio['nombre'] == nombre_apellido:
            del socios[numero_socio]
            print(f"{nombre_apellido} ha sido dado de baja.")

#Función para imprimir el listado de todos los socios
def imprimir_listado_socios(socios):
    print("Listado de socios:")
    for numero_socio, datos_socio in socios.items():
        estado_cuota = "al día" if datos_socio['cuota_al_dia'] else "pendiente"
        print(f"Socio n°{numero_socio}, {datos_socio['nombre']}, ingresó: {datos_socio['ingreso']}, cuota {estado_cuota}.")

#Bucle principal del programa
while True:
    print("\nMenu:")
    print("1. Mostrar cantidad de socios")
    print("2. Registrar pago de cuotas")
    print("3. Modificar la fecha de ingreso")
    print("4. Dar de baja a un socio")
    print("5. Imprimir listado de socios")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        mostrar_cantidad_socios(socios)
    elif opcion == '2':
        numero_socio = int(input("Ingrese el número de socio que ha pagado todas las cuotas adeudadas: "))
        pagar_cuotas(socios, numero_socio)
    elif opcion == '3':
        fecha_antigua = '13/03/2018'
        fecha_nueva = '14/03/2018'
        modificar_fecha_ingreso(socios, fecha_antigua, fecha_nueva)
    elif opcion == '4':
        nombre_apellido = input("Ingrese el nombre y apellido del socio que desea dar de baja: ")
        dar_de_baja(socios, nombre_apellido)
    elif opcion == '5':
        imprimir_listado_socios(socios)
    elif opcion == '6':
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
