from botella import botella
class Botella_plastico (botella):
    def __init__(self, marca, capacidad, tapa, diseño, material, tinte): 
        super().__init__ (marca, capacidad, tapa)
        self.diseño = diseño
        self.material = material
        self.tinte = tinte
    def reutiizar_botella (self):
        print (f"La botella se va reciclar: {self.material}")
    def imprimir_info(self):
        print (f"el diseño es: {self.diseño}")
        print (f"El material es: {self.material}")
        print(f"El color es: {self.tinte}")
        super ().imprimir_info()
        print (f"la tapa padre es: {super().tapa}")
        return "informacion encontrada"
        
    
              
        