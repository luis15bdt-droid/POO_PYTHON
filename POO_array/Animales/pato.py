from animales import Animal
class pata (Animal):
    def __init__(self, especie, nombre, habitat, tamaño, capacidades, personalidad):
        super().__init__(especie, nombre, habitat, tamaño)
        self.capacidades = capacidades
        self.personalidad = personalidad
    def sueño (self):
        print ("Ahorita mismo esta durmiendo")
    def comunicacion (self):
        print ("Se esta intentando comunicar con los perros")
    def informacion(self):
        print ("PATO")
        print (f"Su capacidad mas importante es:")
        print (f"Su personalidad es {self.personalidad}")
        return super().informacion()