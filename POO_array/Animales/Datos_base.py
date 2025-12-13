class Base_Datos:

    def __init__(self):
        self.lista_animales = []
    
    def guardar_objeto(self, nuevo_objeto):
        self.lista_animales.append(nuevo_objeto)

    def agregar_varios_objetos(self, lista_nueva):
        self.lista_animales.extend(lista_nueva)
    
    def imprimir_info(self):
        print("\n" + "="*40)
        print("REGISTRO COMPLETO DE ANIMALES EN BASE DE DATOS")
        print("="*40)
        for objeto in self.lista_animales:
            print(f"Especie: {objeto.especie}")
            print(f"Nombre: {objeto.nombre}")
            print(f"Habitat: {objeto.habitat}")
            print(f"Tamaño: {objeto.tamaño}")
            objeto.informacion() 