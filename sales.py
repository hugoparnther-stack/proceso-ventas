ventas = [
    ("Laptop", 5200),
    ("Mouse", 120),
    ("Monitor", 1800),
    ("Teclado", 250),
    ("Tablet", 2200)
]

def calcular_total(*precios):
    return sum(precios)

def registrar_compra(**datos):
    print(datos)

for producto, precio in ventas:
    print(producto, precio)

total = calcular_total(5200, 120, 1800, 250, 2200)
print("Total:", total)

registrar_compra(nombre="Carlos", ciudad="Bogota", metodo_pago="tarjeta")
