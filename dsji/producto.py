class PRoducto:
    def __init__(self, precio, titulo, autor, editorial, año_edicion, preferencias):
        self.precio = precio
        self.titulo = titulo
        self.autor = autor 
        self.editorial = editorial
        self.año_edicion = año_edicion
        self.preferencias = preferencias 
    def vender (self):
        return ("Su ")
    def comprar (self):
        return ("")
    def ver_Catalogo (self):
        return ("")
    
    def informacion (self):
        print (f"El precio del producto es: {self.precio}")
        print (f"el titutlo del producto es: {self.titulo}")
        print (f"El autor es: {self.autor}")
        print (f"Su editorial es: {self.editorial}")
        print (f"Su año de edicion es {self.año_edicion}")
        print (f"Y sus preferencias son: {self.preferencias}")
        
        