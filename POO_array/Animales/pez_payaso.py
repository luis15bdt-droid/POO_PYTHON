from animales import Animal
class payaso (Animal):
    def __init__(self, especie, nombre, habitat, tamaño, tipo_aleta,tamaño_habitat ):
        super().__init__(especie, nombre, habitat, tamaño)
        self.aleta = tipo_aleta
        self.tamaño_habitat = tamaño_habitat
    def actividad (self):
        print (f"{self.nombre} se encuentra nadando en la pecera")
    def alimentando (self):
        print (r"Esta buscando algo para comer")
    def informacion (self):
        print("PESCADO")
        print (f"Su tipo de aleta es: {self.aleta}")
        print (f"Su pecera es de {self.tamaño_habitat}")
        return super().informacion()