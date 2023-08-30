#Consigna Nº1: Crea una variable llamada "numero1" y asígnale un número entero de tu elección

numero1= 20;
print("[Nº1] ", numero1);

#Consigna Nº2: No borres la variable número uno y crea una variable llamada "numero2" asignándole un número decimal de tu elección.

numero2= 31.5;
print("[Nº2] ", numero2);

#Consigna Nº3: Crear una variable llamada "suma" y almacena la suma de "numero1" y "numero2"

suma= numero1 + numero2
print("[Nº3] ", suma)

#Consigna Nº4: Ahora crear tres variables más sin borrar lo que tienes. Una para resta, otra para multiplicación y otra para división. Imprime estas variables.

resta= numero1 - numero2
multiplicacion= numero1 * numero2
division= numero1 / numero2
print(f"[Nº4] Resta: {resta}; Multiplicación: {multiplicacion}; División: {division}")

#Consigna Nº5: Crea una variable llamada "nombre" y asígnale tu nombre como valor.

nombre= "Joaquín"
print("[Nº5] ", nombre)

#Consigna Nº6: Crea una variable llamada "precio" y asígnale un valor decimal que represente el precio de un artículo ficticio.

precio= 25.5
print("[Nº6] ", precio)

#Consigna Nº7: Ahora, sin borrar la variable anterior, crea una variable llamada "descuento" y asígnale un valor decimal que represente el descuento aplicado al artículo. Por ejemplo, si le quieres aplicar un 25% de descuento, dale un valor de 0,25. El valor 1 equivaldría al 100% y el valor 0 al 0%.

descuento= 0.25
print("[Nº7] ", descuento)

#Consigna Nº8: Ahora, intenta calcular el precio final aplicando el descuento al precio original y almacena el resultado en una variable llamada "precio_final". Para ello vas a tener que aplicar la lógica de matemáticas.

precio_final= precio * descuento
print("[Nº8] ", precio_final)

#Consigna Nº9: Crea una variable llamada "cadena" y asignale un texto, una frase, lo que quieras de tu elección. Qué sea un string.

cadena= "Hola Mundo"
print("[Nº9] ", cadena)

#Consigna Nº10: Sin borrar la variable "cadena", crea una nueva variable llamada "longitud". En ella, vas a almacenar la longitud en caracteres de la cadena utilizando una de las funciones de Python.

longitud= len(cadena)
print("[Nº10] ", longitud)

#Consigna Nº11: Crea otra vez la variable llamada "precio" y dale un valor decimal, el que sea y conviértelo en número entero. Lo puedes hacer en la misma variable o en otra, da lo mismo.

precio= int(90.26)
print("[Nº11] ", precio)

#Consigna Nº12: Crea dos variables. Una se va a llamar "nombre" y la segunda "apellido" concaténalas en una tercera variable llamada "nombre_completo", el nombre y el apellido con un espacio entre medio. Puedes usar libremente la forma de concatenación que quieras.

nombre= "Annya"
apellido= "Forger"
nombre_completo= nombre + " " + apellido
print("[Nº12] ", nombre_completo) 

#Consigna Nº13: Escribe tu edad en una variable. Increméntala en 5 y luego disminúyela en 10.

edad= 20
edad += 5
edad -= 10
print("[Nº13] ", edad)

#Consigna Nº14: Crea una variable llamada "altura" que contenga con decimales, tu altura en metros y centímetros. Por ejemplo: 1.83. Multiplícala por 4 y luego divídela en 3.

altura= 1.87
altura= altura * 4
altura= altura / 3
print("[Nº14] ", altura)

#Consigna Nº15: Crea una variable que contenga tu nombre completamente en mayúsculas. Después transfórmalo todo en minúsculas con algún método o función de Python.

name= "JOAQUÍN GALLO"
minus_name= name.lower()
print("[Nº15] ", name)

#Consigna Nº16: Por último, con la variable con el nombre en mayúsculas, aplica un método parecido para que se transforme todo en minúsculas excepto la primera letra.

final_name= name.capitalize()
print("[Nº16] ", final_name)