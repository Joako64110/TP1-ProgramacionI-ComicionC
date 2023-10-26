from class_m import Motorcycle

#Instanciamiento de las diferentes motocicletas
vehicle1= Motorcycle("Azul", "A12-3BCD", 10, 2, "Honda", "CB 125F 2024", "10/01/2023", "89km/h", "117kg")
vehicle2= Motorcycle("Verde", "F90-1YAP", 15, 2, "Yamaha", "Ténéré 700 Extreme 2024", "30/03/2023", "184km/h", "205kg")
vehicle3= Motorcycle("Negro", "R35-9BXQ", 10, 2, "Susuki", "GSX-8S 2023", "16/06/2023", "215km/h", "202kg") #N1
vehicle4= Motorcycle("Rojo", "L06-5WKE", 8, 2, "Kawasaki", "Ninja 1000 SX 2022", "25/09/2023", "350km/h", "235kg") #N2
vehicle5= Motorcycle("Blanco", "Q86-7JCY", 12, 2, "BMW", "R 1250 GS", "14/02/2023", "200km/h", "249kg")

#Pruebas de arranque y detención del vehicle3 y vehicle4
vehicle3.start_up()
print("----------------------------------------------")
vehicle3.start_up()
print("----------------------------------------------")
vehicle3.stop_engine()
print("----------------------------------------------")
vehicle3.stop_engine()
print("----------------------------------------------")
vehicle4.start_up()
print("----------------------------------------------")
vehicle4.start_up()
print("----------------------------------------------")
vehicle4.stop_engine()
print("----------------------------------------------")
vehicle4.stop_engine()
print("")

#Agregado de precio a la única motocicleta que la compañia ya tiene precio
vehicle4.price= "15.550€"

#Impresión de precio agregado previamente
print(f"El precio de la motocicleta {vehicle4.brand} {vehicle4.model} es de {vehicle4.price}")
print("")

#Conversión de la impresión anterior en un método
def price_inquiry(self):
    print(f"El precio de la motocicleta {self.brand} {self.model} es de {self.price}")

vehicle4.price_inquiry= price_inquiry(vehicle4)