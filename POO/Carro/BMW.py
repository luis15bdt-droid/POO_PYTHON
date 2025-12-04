from carro import Carro
class deportivo (Carro):
    def __init__(self, modelo, color, motor, combustible, velocidad):
        super().__init__(modelo, color, motor)
        self.combustible = combustible
        self.velocidad = velocidad
    def Apagado (self):
        print (f"El auto {self.modelo} se encuentra apagado")
        return " "
    def informacion (self):
        print ("AUTO DEPORTIVO")
        print (f"El tipo de combustible que usa el auto es: {self.combustible}")
        print (f"Y una velocidad maxima de: {self.velocidad}")
        super().informacion()
        return "informacion completada"