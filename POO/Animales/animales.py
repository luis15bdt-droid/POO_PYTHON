class Animal:
    def __init__(self, especie, nombre, habitat, tamaño):
        self.especie = especie
        self.nombre = nombre
        self.habitat = habitat
        self.tamaño = tamaño
    def Interaccion_social (self):
        print (f"El {self.especie} esta acompañado de mas de su misma especie")
    def descanso (self):
        print (f"{self.nombre} se encuentra descansando")
    def informacion (self):
        print (f"Nuestro {self.especie} se llama {self.nombre}")
        print (f"Se encuentra en el habitat{self.habitat}")
        print (f"Es de un tamaño aproximado de {self.tamaño}")
        
        