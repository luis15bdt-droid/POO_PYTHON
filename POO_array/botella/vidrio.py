from botellaa import botella
class vidrioo (botella):
    def __init__ (self, marca, capacidad, tapa, material, forma, grabados, color):
        super().__init__ (marca, capacidad, tapa, material)
        self.forma = forma
        self.grabados = grabados
        self.color = color
    def transparencia (self):
        print (f"Contiene una transparencia es de color {self.color}")
    def informacion (self):
        print ("BOTELLA DE VIDRIO")
        print (f"La botella tiene una transparencia de color {self.color}")
        print (f"tiene con una forma {self.forma}")
        print (f"la botella incluye {self.grabados}")
        print (f"tiene un color {self.color}")
        super().informacion()
        