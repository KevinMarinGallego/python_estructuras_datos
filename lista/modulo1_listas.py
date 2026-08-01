# ==========================
# INVENTARIO
# ==========================

inventario = [
    ["Mouse", 10, 25000],
    ["Teclado", 5, 80000],
    ["Monitor", 3, 650000]
]

# ==========================
# ACTUALIZAR PRECIO
# ==========================

def actualizar_precio(producto, nuevo_precio):
    for item in inventario:
        if item[0] == producto:
            item[2] = nuevo_precio
            print(f"El precio de {producto} fue actualizado a ${nuevo_precio}")
            return

    print("Producto no encontrado.")


# ==========================
# REGISTRAR VENTA
# ==========================

def registrar_venta(producto, cantidad):

    for item in inventario:

        if item[0] == producto:

            if item[1] >= cantidad:
                item[1] -= cantidad
                print(f"Venta realizada de {cantidad} unidades de {producto}")
            else:
                print("No hay suficiente stock.")

            return

    print("Producto no encontrado.")


# ==========================
# AÑADIR PRODUCTO
# ==========================

def anadir_producto(producto, cantidad, precio):

    for item in inventario:

        if item[0] == producto:
            item[1] += cantidad
            print(f"Se agregaron {cantidad} unidades al stock de {producto}")
            return

    inventario.append([producto, cantidad, precio])

    print(f"Producto {producto} agregado al inventario.")


# ==========================
# MOSTRAR INVENTARIO
# ==========================

def mostrar_inventario():

    print("\n===== INVENTARIO =====")

    for item in inventario:

        print(f"Producto: {item[0]}")
        print(f"Cantidad: {item[1]}")
        print(f"Precio: ${item[2]}")
        print("------------------------")


# ==========================
# LLAMADO DE FUNCIONES
# ==========================

actualizar_precio("Teclado", 90000)

registrar_venta("Mouse", 2)

anadir_producto("Impresora", 4, 450000)

mostrar_inventario()