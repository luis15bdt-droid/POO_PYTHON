from animales import Animal
class Caballo (Animal):
    def __init__(self, especie, nombre, habitat, tamaño, dieta, color):
        super().__init__(especie, nombre, habitat, tamaño)
        self.dieta = dieta
        self.color = color
    def alimentacion (self):
        print (f"{self.nombre} Se alimenta de {self.dieta}")
    def temperamento (self):
        print (f"Aunque sea {self.color} es bastante tranquilo")
    def informacion(self):
        print ("CABALLO")
        print (f"Su dieta es principalmente {self.dieta}")
        print (f"Es de un color {self.color}")
        return super().informacion()
    
        