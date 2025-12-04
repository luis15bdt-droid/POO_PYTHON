class botella:
    def __init__ (self, marca, capacidad, tapa, material):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa 
        self.material = material
    def llenar_botella(self, capacidad):
        print(f"La botella se está llenando: {capacidad}")
        print(f"Se va a usar la tapa: {self.tapa}")
    
    def cerrar_tapa(self, dato_cantidad):
        print(f"Se uso la tapa: {self.tapa}")
        print(f"Cantidad de tapas usadas: {dato_cantidad}")
        return dato_cantidad
    
    def informacion (self):
        print(f"La marca es: {self.marca}")
        print(f"Tipo de tapa es: {self.tapa}")
        print(f"La capacidad de la botella es: {self.capacidad}")
        print (f"Tipo de material {self.material}")