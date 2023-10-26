class Motorcycle:

    new= True
    engine= False

    def __init__(self, color, tuition, fuel_liters, wheels_number, brand, model, manufacturing_date, top_speed, weight):
        self.color= color
        self.tuition= tuition
        self.fuel_liters= fuel_liters
        self.wheels_number= wheels_number
        self.brand= brand
        self.model= model
        self.manufacturing_date= manufacturing_date
        self.top_speed= top_speed
        self.weight= weight
    
    def start_up(self):
        if (self.engine == True):
            print("El motor ya está en marcha.")
        else:
            print("---<Encendiendo motor>---")
            self.engine= True
            print("---<Motor encendido con éxito>---")
    
    def stop_engine(self):
        if (self.engine == False):
            print("El motor ya se encuentra apagado.")
        else:
            print("---<Deteniendo motor>---")
            self.engine= False
            print("---<Motor detenido con éxito>---")
    