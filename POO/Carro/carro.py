class Carro:
    def __init__(self, modelo, color, motor):
        self.modelo = modelo
        self.color = color
        self.motor = motor
        
    def climatizacion(self):
        return "Sistema de aire acondicionado básico."
    def luces(self):
        return "Luces delanteras y traseras operativas."
    
    def informacion (self):
        print (f"El modelo del auto es: {self.modelo}")
        print (f"De un color: {self.color}")
        print (f"El {self.modelo} tiene un motor {self.motor}")
        