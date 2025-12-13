from producto import PRoducto
class segunda_mano (PRoducto):
    def __init__(self, precio, titulo, autor, editorial, año_edicion, preferencias, clasificacion, tema, vendedor):
        super().__init__(precio, titulo, autor, editorial, año_edicion, preferencias)
        self.clasificacion = clasificacion 
        self.tema = tema
        self.vendedor = vendedor
