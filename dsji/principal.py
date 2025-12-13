from producto import PRoducto
from libro import LbrO
from revista import REvista
from segunda_MAno import segunda_mano
from articulo_online import ARticuloOnline
from novedades import Novedades
from usuario import USuario
from editorial import eleditorial
from procesador import elprocesador
from servidor import elservidor
from indexador import elindexador
from recolector import elrecolector
from hilo import elhilo

print("Productos")
generico = PRoducto(25000, "Cuento", "Anonimo", "Base Editores", 2009, ["Drama"])

print(generico.ver_Catalogo())




libro = LbrO(35000, "El arte de ser nosotros", "Inma Rubiales", "Editorial Sudamericana", 2009, ["Clasico"], "Novela")
print(libro.comprar())

revista = REvista(50000, "Las cronicas de narnia", "C. S. Lewis", "TechPress", 1967, ["Clasico"], "Novela")
print(revista.vender())


art_segunda_mano = segunda_mano(15000, "El príncipe Caspia USADO", "C. S. Lewis", "Pearson", 1951, ["Fantasia"], "Cuento", "Fantasia", "Cucho Vendedor")

art_online = ARticuloOnline(9000, "Nacho lee", "Educacion primaria", "Jorge Luis Osorio Quijano", 2000, ["Educativo"], "Lenguajes")

novedad_reciente = Novedades(40000, "Hábitos Atómicos", "James Clear", "Curar malos habitos", 2018, ["Ciencia"], "Lanzamiento", "Autoayuda")
novedad_reciente.cambiar_clasificacion() 


print("\n" + "-"*30)


print(" Creacion de Actores y Sistemas")
usuario = USuario("Nestor", "Parra", "32123", "Atalaya", "nespa", "nestor21")

editorial_socia = eleditorial("Cocobongo", "Av. Antonia santos", "3208375313")

procesador_ventas = elprocesador()

servidor_principal = elservidor()

indexador_data = elindexador()
recolector_noticias = elrecolector()
hilo_fondo = elhilo()


print("\n" + "-"*30)


print(" Flujo de Compra")
print(usuario.compra()) 

servidor.datos_Compra()

procesador_ventas.realizar_cobro()
print(libro.comprar())

print("\n" + "-"*30)

print("Flujo de Venta")
editorial_socia.vender()

servidor.datos_venta()

procesador_ventas.mandar_datos_Venta()
procesador_ventas.realizar_pago()
print(revista.vender())

print("\n" + "-"*30)


print(" Flujo de Sugerencia")
print(usuario.sugerencia())

servidor.sugerencias()

procesador_ventas.envia_sugerencia_admin()

print("\n" + "-"*30)

print("Flujo de Mantenimiento y Busqueda")

servidor_principal.muestra_pag()

hilo_fondo.busca_novedades()

recolector_noticias.envia_novedades()

indexador_data.actualiza_almacen()
procesador_ventas.modificar_stock()

procesador_ventas.actualiza_catalogo()

procesador_ventas.realizar_busqueda()
indexador_data.envia_resultado_busqueda()
