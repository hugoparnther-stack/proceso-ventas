# Ejercicio: procesar ventas con *args y **kwargs

ventas = [
    ("Laptop", 5200),
    ("Mouse", 120),
    ("Monitor", 1800),
    ("Teclado", 250),
    ("Tablet", 2200)
]

# suma cualquier cantidad de precios que le pasemos
def calcular_total(*precios):
    total = 0
    for p in precios:
        total += p
    return total

# recibe datos del cliente, pueden ser los que sea
def registrar_compra(**datos):
    print("Datos del cliente:")
    for key in datos:
        print(key, "->", datos[key])


# lista de precios sacados de la lista de ventas
precios = []
for producto, precio in ventas:
    precios.append(precio)

print("Ventas:")
for producto, precio in ventas:
    print(producto, precio)

total_ventas = calcular_total(*precios)
print("Total:", total_ventas)

# prueba con otros numeros sueltos
print(calcular_total(10, 20, 30))

registrar_compra(nombre="Carlos", ciudad="Bogota", metodo_pago="tarjeta")
registrar_compra(nombre="Maria", ciudad="CDMX", metodo_pago="efectivo", producto="Laptop")
