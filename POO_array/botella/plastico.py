from botellaa import botella
class Botella_plastico (botella):
    def __init__(self, marca, capacidad, tapa, material, diseño, tinte): 
        super().__init__ (marca, capacidad, tapa, material)
        self.diseño = diseño
        self.tinte = tinte
    def reutiizar_botella (self):
        print (f"La botella se va reciclar: {self.material}")
    def informacion(self):
        print ("BOTELLA PLASTICA")
        print (f"el diseño es: {self.diseño}")
        print(f"El color es: {self.tinte}")
        super ().informacion()
        print (f"la tapa padre es: {self.tapa}")
        return "informacion completada"
        
    
              
        