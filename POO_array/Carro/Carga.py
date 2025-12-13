from carro import Carro
class Carga (Carro):
    def __init__(self, modelo, color, motor, max_carga, puertas):
        super().__init__(modelo, color, motor)
        self.max_carga = max_carga
        self.puertas = puertas
    def Sistema_direccion (self):
        print ("Este vehiculo utiliza un sistema de direccion hidraulico")
    def informacion (self):
        print ("VEHICULO DE CARGA")
        print (f"El vehiculo cuenta con una carga maxima de {self.max_carga}")
        print (f"Cuenta con un total de: {self.puertas} puertas")
        super().informacion()
        return "informacion completada"