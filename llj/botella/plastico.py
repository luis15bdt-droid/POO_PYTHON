from botella import botella
class Botella_plastico ():
    def __init__(self, marca, capacidad, tapa): 
        super __init__ (marca, capacidad, tapa)
        self.diseno = ""
        self.material = ""
        self.tinte = ""
    def reutiizar_botella (self):
        print (f"La botella se va reciclar: {self.material}")
    def imprimir_info(self):
        print (f"el diseño es: {self.diseno}")
        print (f"El material es: {self.material}")
        print(f"El color es: {self.tinte}")
        super ().imprimir_info()
        print (f"la tapa padre es: {super().tapa}")
        return "informacion encontrada"
        
    
              
        