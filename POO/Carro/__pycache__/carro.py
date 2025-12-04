class Carro ():
    def Datos (self, Modelo, Color, Motor, Combustible):
        self.modelo = Modelo
        self.color = Color 
        self.motor = Motor
        self.combustible = Combustible
    def Datos_Motor (self, Motor ):
        print (f"Se va a usar el motor {Motor}")
        print (f"El cual usa combustible{self.combustible}")
        
    def Mostrar_info (self):
        print (f"El modelo del vehiculo e: {self.modelo}")
        print (f"De un color {self.color}")
        print ("Usando un potente motor: {self.motor}")
        print (f"Y por ultimo usando como combustible {self.combustible}")
        