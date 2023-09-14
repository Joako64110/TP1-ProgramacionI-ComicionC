#El usuario ingresa la fecha en un formato específico.

fecha= input("Ingrese la fecha actual en el siguiente formato <dia, ND/NM>: ")
week= ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
total= 0
amount= ""
tariff= ""
day= ""
num_day= ""
num_month= ""
aux= ""


#Se compruba que el usuiario haya brindado los datos solicitados y el formato correcto de ésto.

helper= fecha.split(", ")
if (len(helper) != 2):
    exit("Por favor, ingrese la fecha en el formato indicado")
else:
    day= helper[0].lower()
    aux= helper[1]
    if (aux[1].isdigit() != True):
        exit("Por favor, ingrese el número del día usando dos numeros. (Ejemplo: 06/09)")
    else:
        num_day= aux[0] + aux[1]
        if (len(aux) != 4):
            if (aux[4].isdigit() != True):
                exit("Por favor, ingrese el número del día usando dos numeros. (Ejemplo: 06/09)")
            else:
                num_month= aux[3] + aux[4]
        else:
            exit("Por favor, ingrese el número del día usando dos numeros. (Ejemplo: 06/09)")

for i in week:
    if (day == i):
        aux= True
        break
    else:
        aux= False

if (aux == True):
    print("Nombre del día: Aceptado")
elif (aux == False):
    exit("Día inexistente, por favor, ingrese un día válido")
aux= ""

if (num_day.isdigit()):
    num_day= int(num_day)
    if (num_day <= 31 and num_day > 0):
        print("Número del día: Aceptado")
    else:
        exit("Número del día inválido")
else:
    exit("Por favor, asegurece de que lo que ingresó sea un número")

if (num_month.isdigit()):
    num_month= int(num_month)
    if (num_month <= 12 and num_month > 0):
        print("Número del mes: Aceptado")
    else:
        exit("Número del mes inválido")
else:
    exit("Por favor, asegurece de que lo que ingresó sea un número")

#El usuario ingresa los datos relacionados a la actividad del día.

print("¿El día de hoy a qué actividad corresponde? (A= Exámenes de Nivel Inicial, Intermedio, Avanzado; B= Práctica Hablada; C= Inglés para Pasajeros)")
choose= input().lower()

if (choose == "a"):
    choose= input("Ingrese la cantidad de alumnos que aprobaron el exámen: ")
    if (choose.isdigit() != True):
        exit("Por favor, ingrese un número entero")
    choose_2= input("Ingrese la cantidad de alumnos que desaprobaron el exámen: ")
    if (choose_2.isdigit() != True):
        exit("Por favor, ingrese un número entero")
    choose= int(choose)
    choose_2= int(choose_2)
    average= (choose + choose_2) / 2
    print(f"El porcentaje de alumnos aprobados es de {average}%")
elif (choose == "b"):
    choose= input("Ingrese el porcentaje de asistencia de la clase (sin el símbolo <%>): ")
    if (choose.isdigit() != True):
        exit("Por favor, ingrese un número entero")
    choose= int(choose)
    if (choose > 50):
        print("Asistío la mayoría")
    else:
        print("No asistió la mayoría")
elif (choose == "c"):
    aux_d= int(helper[1][1])
    aux_m= int(helper[1][4])
    if ((aux_d == 1) and ((aux_m == 1) or (aux_m == 7))):
        print("Comienzo de nuevo ciclo")
        amount= input("Ingrese la cantidad de alumnos del nuevo ciclo: ")
        if (amount.isdigit() != True):
            exit("Por favor, ingrese un número entero")
        else:
            amount= int(amount)
        tariff= input("Ingrese el arancel por acada alumno: ")
        if (tariff.isdigit() != True):
            exit("Por favor, ingrese un número real")
        else:
            tariff= int(tariff)
        total= tariff * amount
        print(f"El ingreso total es de {total}$")
    else:
        print("error")
else:
    exit("Por favor, ingrese una de las opciones propuestas, es decir, <a>, <b> ó <c>")