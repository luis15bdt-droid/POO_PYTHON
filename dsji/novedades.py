from producto import PRoducto
class Novedades (PRoducto):
    def __init__(self, precio, titulo, autor, editorial, año_edicion, preferencias, clasificacion, tema):
        super().__init__(precio, titulo, autor, editorial, año_edicion, preferencias) 
        self.clasificacion = clasificacion
        self.tema = tema
    def cambiar_clasificacion (self):
        print (f"Su clasificacion ha cambiado a {self.clasificacion}")
    def informacion(self):
        print ("             ")
        print ("NOVEDADES")
        print (f"Su clasificacion actual es: {self.clasicacion}")
        print (f"Y su tem es {self.tema}")
        return super().informacion()