#--------------------Ejercicio 1--------------------

from Clases.class_persona import Persona

persona1 = Persona("Lucas", 16, "44349212")
persona1.mostrar()
persona1.legalage()

##--------------------Ejercicio 2--------------------

from Clases.class_cuenta import Cuenta

cuenta1= Cuenta("Mariano Gonzales", 5000.00)
print(cuenta1.get_owner())
print(cuenta1.get_amount())
cuenta1.set_owner("María Lopez")
cuenta1.set_amount(7500.00)
cuenta1.show()
cuenta1.deposit(1500.50)
cuenta1.withdraw(4000.00)

##--------------------Ejercicio 3--------------------

from Clases.class_triangle import Triangle

side1, side2, side3= 12, 30, 15

triangle1 = Triangle(side1, side2, side3)
print(f"El lado más largo del triángulo es {triangle1.longest_side()}")
print(f"El triángulo es de tipo {triangle1.triangle_type()}")

#--------------------Ejercicio 4--------------------

from Clases.class_addressbook import AddressBook

address_book = AddressBook()
address_book.menu()