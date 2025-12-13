class USuario:
    def __init__(self, nombre, apellido, n_cuenta, direccion, login, password):
        self.nombre = nombre
        self.apellido = apellido
        self.n_cuenta = n_cuenta
        self.direccion = direccion 
        self.login = login
        self.password = password
    def sugerencia (self):
        return (f"{self.nombre} {self.apellido} Ha enviado una sugerencia")
    def leer (self):
        return(f"{self.nombre} {self.apellido} se encuentra leyendo ")
    def compra (self):
        return (f"{self.nombre} {self.apellido} ha realizado una compra")
    def vender (self):
        return ("{self.nombre} {self.apellido} ha vendido un producto")
    def reclamo (self):
        return ("{self.nombre} {self.apellido} Esta realizando un reclamo")
    
    
        

