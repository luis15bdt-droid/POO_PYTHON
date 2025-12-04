from producto import PRoducto
class LbrO (PRoducto):
    def __init__(self, precio, titulo, autor, editorial, año_edicion, preferencias, genero):
        super().__init__(precio, titulo, autor, editorial, año_edicion, preferencias)
        self.genero = genero
    def informacion(self):
        print (f"El genero de {self.autor} es {self.genero}")
        return super().informacion()
    
