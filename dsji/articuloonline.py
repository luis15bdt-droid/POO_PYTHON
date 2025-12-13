from producto import PRoducto
class ARticuloOnline (PRoducto):
    def __init__(self, precio, titulo, autor, editorial, año_edicion, preferencias, tema):
        super().__init__(precio, titulo, autor, editorial, año_edicion, preferencias)
        self.tema = tema
    def publicar (self):
        return (f"El libro se ha publico con exito hoy {self.año_edicion}")
