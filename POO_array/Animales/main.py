from caballo import Caballo
from cocodrilo import Cocodrilo
from pato import pata
from pez_payaso import payaso
from Datos_base import Base_Datos 
from animales import Animal 

lista_animales_iniciales = [
    Caballo("Caballo", "Myke", "Praderas", "14m", "Hierva", "Negro"),
    Cocodrilo("Cocodrilo", "Cuco", "Rios", "4Metros", "430kg", "8 años"),
    pata("Pato", "Anuel", "Estanques", "58cm", "Volar", "Agresiva"),
    payaso("Pez", "Nemo", "Oceano", "7cm", "Aleta Dorsal", "10m de profundidad")
]



print()

gestor_db = Base_Datos()

gestor_db.agregar_varios_objetos(lista_animales_iniciales)
print("Creacion y Guardado de Nuevo Animal:")
nueva_especie = input("Escriba la especie del animal: ")
nuevo_nombre = input("Escriba el nombre del animal: ")
nuevo_habitat = input("Escriba el habitat: ")
nuevo_tamaño = input("Escriba el tamaño aproximado: ")

animal_nuevo_input = Animal(nueva_especie, nuevo_nombre, nuevo_habitat, nuevo_tamaño)


gestor_db.guardar_objeto(animal_nuevo_input)
print(f"¡Animal {nuevo_nombre} ({nueva_especie}) agregado con éxito!")

gestor_db.imprimir_info()