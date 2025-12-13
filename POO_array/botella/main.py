from plastico import Botella_plastico
from vidrio import vidrioo
from Base_datos import Base_Datos
from botellaa import botella
### CODIGO PRINCIPAL ####
### INSTNACIA HIJA ###
objBotella_Plastica = Botella_plastico ("Pepsi", "500ML", "Comun", "Plastico", "Redondo", "Sin tinte")
Botella_vidrio = vidrioo ("7UP", "1Litro", "Raro", "Vidrio", "Cilindrica", "Logo", "Verde")

objBotella_Plastica.reutiizar_botella()
objBotella_Plastica.informacion()


Botella_vidrio.transparencia()
Botella_vidrio.informacion()
print()

obj_base_datos = Base_Datos()

obj_base_datos.guardar_objeto(objBotella_Plastica)
obj_base_datos.guardar_objeto(Botella_vidrio)

print("Ingrese aqui su Botella")
nueva_marca = input("Escriba la marca de la botella: ")
nueva_capacidad = input("Escriba la capacidad: ")
nueva_tapa = input("Escriba el tipo de tapa: ")
nuevo_material = input("Escriba el material: ")
botella_nueva_input = botella(nueva_marca, nueva_capacidad, nueva_tapa, nuevo_material)

obj_base_datos.guardar_objeto(botella_nueva_input)
print(f"\n¡Botella de marca '{nueva_marca}' ({nuevo_material}) agregada con éxito!")

obj_base_datos.imprimir_info()