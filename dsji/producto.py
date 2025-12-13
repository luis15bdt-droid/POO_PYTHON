class PRoducto:
    def __init__(self, precio, titulo, autor, editorial, año_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor 
        self.editorial = editorial
        self.año_edicion = año_edicion
        self.preferencias = preferencias 
    def vender (self):
        return (f"Su libro a sido vendido por {self.precio} ")
    def comprar (self):
        return (f"Usted ha comprado {self.titulo} por {self.precio}")
    def ver_Catalogo (self):
        return ("Usted esta viendo el catalogo")

        
