"""
Script para procesar ventas.

Incluye:
- Lista de ventas (producto, precio).
- calcular_total(*precios): suma cualquier cantidad de precios.
- registrar_compra(**datos): registra información del cliente (nombre, ciudad,
  método de pago, etc.) de forma flexible.
"""

ventas = [
    ("Laptop", 5200),
    ("Mouse", 120),
    ("Monitor", 1800),
    ("Teclado", 250),
    ("Tablet", 2200),
]


def calcular_total(*precios):
    """Suma cualquier cantidad de precios recibidos como argumentos posicionales."""
    return sum(precios)


def registrar_compra(**datos):
    """
    Registra la información de una compra a partir de datos arbitrarios del cliente.
    Ejemplo de uso: registrar_compra(nombre="Ana", ciudad="Lima", metodo_pago="Tarjeta")
    """
    print("Registro de compra:")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")
    print()
    return datos


def main():
    print("=== Lista de ventas ===")
    for producto, precio in ventas:
        print(f"  {producto}: ${precio}")
    print()

    # calcular_total con los precios de la lista de ventas
    precios = [precio for _, precio in ventas]
    total = calcular_total(*precios)
    print(f"Total de ventas: ${total}\n")

    # calcular_total con cualquier cantidad de argumentos
    print(f"Ejemplo suelto: calcular_total(100, 200, 300) = {calcular_total(100, 200, 300)}\n")

    # registrar_compra con distintos datos de cliente
    registrar_compra(
        nombre="Carlos Pérez",
        ciudad="Bogotá",
        metodo_pago="Tarjeta de crédito",
        producto="Laptop",
        total=5200,
    )

    registrar_compra(
        nombre="María Gómez",
        ciudad="Ciudad de México",
        metodo_pago="Efectivo",
    )


if __name__ == "__main__":
    main()
