from animales import Animal
class Cocodrilo (Animal):
    def __init__(self, especie, nombre, habitat, tamaño, peso, edad ):
        super().__init__(especie, nombre, habitat, tamaño)
        self.peso = peso
        self.edad = edad
    def personalidad (self):
        print (f"Hoy esta agresivo")
    def descanso (self):
        print ("Se esta moviendo")
    def informacion (self):
        print ("COCODRILO")
        print (f"Tiene un peso total de: {self.peso}")
        print (f"Tiene {self.edad} años")
        return super().informacion()
    
