class Botella:
    def __init__(self, marca, capacidad, tapa):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa
    def llenar_botella (self, capacidad):
        print (f"LA botella esta llenandose: {capacidad}")
        print (f"Se va a usar la tapa {self.tapa}")
    def cerrar_tapa (self, dato_cantidad):
        print (f"Se uso la tapa {self.tapa}")
        print (f"Cantidad de tapas usadas {dato_cantidad}")
        return dato_cantidad
    def imprimir_info (self):
        ####+ Metodo informacion de los atributos ### +
        print (f"la marca es: {self.marca}")
        print (f"Tipo de tapa es: {self.tapa}")
        print (f"La capacidad de la botella es de: {self.capacidad}")
        
        