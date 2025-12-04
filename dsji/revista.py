from producto import PRoducto
class REvista (PRoducto):
    def __init__(self, precio, titulo, autor, editorial, año_edicion, preferencias, categoria):
        super().__init__(precio, titulo, autor, editorial, año_edicion, preferencias)
        self.categoria = categoria 
    def informacion(self):
        print ("La categoria del producto es: {self.categoria}")
        return super().informacion()