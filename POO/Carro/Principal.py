from BMW import deportivo
from Carga import Carga

def main ():
    BMWDeportivo = deportivo ("BMW M340i", "Negro", "B58", "Gasolina", "250km/h")
    carga = Carga ("Silverado 1500", "Blanco", "Duramax Turbo-Diesel I6", "986kg", "4")
    print (BMWDeportivo.informacion())
    print (BMWDeportivo.Apagado())
    
    
    print (carga.informacion())
    print (carga.Sistema_direccion())
    
main()