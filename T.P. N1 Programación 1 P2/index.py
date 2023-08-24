#--------------------Ejercicio 2--------------------

cateto1= float(input("Ingrese el valor del cateto 1: "))
cateto2= float(input("Ingrese el valor del cateto 2: "))
hipotenusa= ((cateto1*2)+(cateto22))*(1/2)
print("La hipotenusa del triángulo es: ",hipotenusa)

#--------------------Ejercicio Nº3--------------------

num1=float(input('ingrese el primer numero '))
num2=float(input('ingrese el segundo número '))
suma=num1+num2
print(suma)
resta=num1-num2
print(resta)
multiplicacion=num1*num2
print(multiplicacion)
division=num1/num2
print(division)

#--------------------Ejercicio Nº4--------------------

farenh = float(input("Ingrese los grados fahrenheit: "))
celsius = (farenh-32)*5/9
print(f"El equivalente en celsius de {farenh}°F es: {celsius}°C")

#--------------------Ejercicio Nº5--------------------

#	a) A = input(nombre, “¿Cuál es tu canción favorita?”)
# El error se encuentra en que input no puede recibir dos argumentos
# Solucion: Sacando la variable "nombre"

# b)	precio = input(“Precio: “)
# total = precio + (precio * 0.1)
# El error se encuentra en que input devuelve una string, 
# y una string no puede ser multiplicada, ni ser sumada a otros numeros
# Solucion: usando int en el input, quedando: int(input("Precio: "))

# c)	edad = int(input(“Edad: “))
# print(tu edad es, edad)
# El error esta en el print, el cual no tiene "" representando una string, 
# baisamente le esta pasando de forma erronea los argumentos
# Solucion: agregando comillas de esta forma: print("tu edad es", edad)

# d)	edad = int(input(“Edad: “))
# print(“Veamos si tu edad es 18…”, edad=18)
# El error esta en que no es valido el argumento que se le pasa, "edad=18", ademas de que un solo igual
# representa asignacion.
# La solucion seria usar un if else, con la condicion "edad==18"
# algo asi: 
# edad = int(input("Edad: "))
# if edad == 18:
#  print("Veamos si tu edad es 18… Tienes 18 años")
# else:
#   print("tu edad no es 18 años")

#--------------------Ejercicio Nº6--------------------

num = 0
suma = 0
for i in range(3):
    num = float(input(f"Ingrese la el numero {i+1}: "))
    suma = suma + num
print(f"Media: {suma/3}")

#--------------------Ejercicio Nº7--------------------

valor= int(input("Ingrese la cantidad de minutos que desee: "))

minutos= valor % 60
horas= (valor - minutos)/60
print(f"{valor} minutos son {horas} horas y {minutos} minutos")

#--------------------Ejercicio Nº8--------------------

sueldo_base = float(input("Ingrese el sueldo base: "))
#cantidad_ventas = int(print("Ingrese cantidad de ventas:) "))
cantidad_ventas = 3
comision = 0.1*cantidad_ventas*sueldo_base
sueldo_total = sueldo_base + comision
print(f"Total de dinero en comisiones $ {comision} \nRemuneracion total de salario mas comision es: ${sueldo_total}")

#--------------------Ejercicio Nº9--------------------

compra= float(input("Ingrese el valor de su compra: "))
descuento= 0.15
total= compra-(compra*descuento)
print("El total de su compra con descuento es de: ",total)

#--------------------Ejercicio Nº10--------------------

parcial1=float(input('ingrese la nota del primer parcial: '))
parcial2=float(input('ingrese la nota del segundo parcial: '))
parcial3=float(input('ingrese la nota del tercer parcial: '))

notas_parcial = (parcial1+parcial2+parcial3)/3

examen_final=float(input('ingrese la nota del examen final: '))

trabajo_final=float(input('ingrese la nota del trabajo final: '))

promedio=(notas_parcial * 0.55) + (examen_final * 0.30) + (trabajo_final * 0.15)

print('el promedio de todas tus notas es de: ', promedio)

#--------------------Ejercicio Nº11--------------------

num1 = float(input("Ingrese numero 1: "))
num2 = float(input("Ingrese numero 2: "))

dist = abs(num1 - num2)

print(f"La distancia entre {num1} y {num2} es: {dist}")

#--------------------Ejercicio Nº12--------------------

numero = float(input("Ingrese un numero: "))

r_cuadrada = numero**1/2
r_cubica = numero**1/3

print(f"La raiz cuadrada de {numero} es: {r_cuadrada} y su raiz cubica es: {r_cubica}")

#--------------------Ejercicio Nº13--------------------

num = input("Ingrese un número:")
inversa = ""
for i in range(len(num)):
    inversa += num[len(num) - 1 - i]
print(f"num: {num}")
print(f"Inversa: {inversa}")

#--------------------Ejercicio Nº14--------------------

numero_a= int(input("Ingrese el primer número que desee: "))
numero_b= int(input("Ingrese el segundo número que desee: "))

numero_h= numero_a
numero_a= numero_b
numero_b= numero_h
print(f"El primer número ingresado cambió a {numero_a} y el segundo número ingresado cambió a {numero_b}")

#--------------------Ejercicio Nº15--------------------

hora_inicial = int(input("Ingrese la hora de salida: "))
minuto_inicial = int(input("ingrese el minuto de salida: "))
segundo_inicial = int(input("ingrse el segundo de salida: "))
tiempo_viaje = int(input("Ingrese en segundos el tiempo de viaje: "))
horas = tiempo_viaje//3600
minutos = (tiempo_viaje%3600)//60
segundos = tiempo_viaje%60
segundo_final = (segundo_inicial + segundos)%60
minuto_final = (minuto_inicial+ (segundo_inicial + segundos)//60+minutos)%60
hora_final = (hora_inicial+horas+(minuto_inicial+(segundo_inicial + segundos)//60+minutos)//60)%24
print(f"Hora de salida:   {hora_inicial} hs  {minuto_inicial} min {segundo_inicial} seg")
print(f"Hora de llegada:   {hora_final} hs {minuto_final} min {segundo_final} seg")

#--------------------Ejercicio Nº16--------------------

nombre= input("Ingrese su nombre: ")
apellido1= input("Ingrese su primer apellido: ")
apellido2= input("Ingrese su segundo apellido: ")
iniciales= nombre[0],apellido1[0],apellido2[0]
print("Sus iniciales son: ",iniciales)

#--------------------Ejercicio Nº17--------------------

usuario=input('ingrese su nombre: ')
print('ahora estás en la matrix, ', usuario)

#--------------------Ejercicio Nº18--------------------

valor_cena = float(input("Ingrese el valor de la cena: "))
cost_serv = (valor_cena * 6.2)/100
propi = (valor_cena * 10)/100
print(f"El valor de la cena, sumando el costo de servicio y la propina es: {valor_cena + cost_serv + propi}")

#--------------------Ejercicio Nº19--------------------

dia = int(input("Ingrese el dia de tu nacimiento: "))
mes = int(input("Ingrese el mes de tu nacimiento: "))
año = int(input("Ingrese el año de tu nacimiento: "))

print(f"El dia de tu nacimiento es: {dia}/{mes}/{año}")

#--------------------Ejercicio Nº20--------------------

fecha = ""
fecha = input("Día de Nacimiento: ")
fecha += input("Mes de Nacimiento: ")
fecha += input("Año de Nacimiento: ")
print(f"Fecha: {fecha}")

#--------------------Ejercicio Nº21--------------------

km_1litro= int(input("Ingrese la cantidad kilómetros que su moto recorre con 1L de combustible: "))
capacidad= int(input("Ingrese la cantidad de litros que posee su tanque de combustible: "))
trayecto= int(input("Ingrese la cantidad de kilometros que desea recorrer: "))
km_tanque= 0
t_requeridos= 0

##Calculo la cantidad de kilómetros que hago con un solo tanque
km_tanque= km_1litro*capacidad
##Calculo los tanques necesarios para el trayecto deseado y lo redondeo
t_requeridos= trayecto/km_tanque
t_requeridos= round(t_requeridos)
print(f"Usted necesitará {t_requeridos} tanques de conbustible para realizar los {trayecto}Km deseados.")