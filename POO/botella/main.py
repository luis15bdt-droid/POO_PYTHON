from plastico import Botella_plastico
from vidrio import vidrioo
### CODIGO PRINCIPAL ####
### INSTNACIA HIJA ###
objBotella_Plastica = Botella_plastico ("Pepsi", "500ML", "Comun", "Plastico", "Redondo", "Sin tinte")
Botella_vidrio = vidrioo ("7UP", "1Litro", "Raro", "Vidrio", "Cilindrica", "Logo", "Verde")

objBotella_Plastica.reutiizar_botella()
objBotella_Plastica.informacion()


Botella_vidrio.transparencia()
Botella_vidrio.informacion()
