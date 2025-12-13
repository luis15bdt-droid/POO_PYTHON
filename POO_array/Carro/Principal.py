from BMW import deportivo
from Carga import Carga
from carro import Carro
from Base_datos import Base_Datos

BMWDeportivo = deportivo ("BMW M340i", "Negro", "B58", "Gasolina", "250km/h")
carga = Carga ("Silverado 1500", "Blanco", "Duramax Turbo-Diesel I6", "986kg", "4")

print (BMWDeportivo.informacion())
print (BMWDeportivo.Apagado())

print (carga.informacion())
print (carga.Sistema_direccion())

print()
print()
print()

obj_base_datos = Base_Datos()

obj_base_datos.guardar_objeto(BMWDeportivo)
obj_base_datos.guardar_objeto(carga)

print("Guarda tu carro")
nuevo_modelo = input("Ingrese el modelo del vehículo: ")
nuevo_color = input("Ingrese el color del vehículo: ")
nuevo_motor = input("Ingrese el tipo de motor: ")

obj_carro_input = Carro(nuevo_modelo, nuevo_color, nuevo_motor)

obj_base_datos.guardar_objeto(obj_carro_input)
print(f"\n¡Carro modelo '{nuevo_modelo}' agregado con exito!")

obj_base_datos.imprimir_info()