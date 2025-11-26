from plastico import Botella_plastico
### CODIGO PRINCIPAL ####
### INSTANCIA DEL PADRE #### 
objBotella = ("Coca-Cola", "1.5L", "Especial")
### INSTNACIA HIJA ###
objBotella_Plastica = Botella_plastico ("Pepsi", "500ML", "Comun", "Redondo", "Plastico", "Sin tinte")
dato_out = objBotella_Plastica.imprimir_info()
print (dato_out)