# ==========================================
# DATASET DE VENTAS
# ==========================================

ventas = [
    ("Laptop", 5, 800, "Tecnología"),
    ("Mouse", 20, 25, "Tecnología"),
    ("Teclado", 15, 45, "Tecnología"),
    ("Silla", 4, 150, "Muebles"),
    ("Escritorio", 3, 300, "Muebles"),
    ("Audífonos", 12, 70, "Tecnología")
]

# ==========================================
# LIST COMPREHENSION
# ==========================================

valor_total = [
    unidades * precio
    for producto, unidades, precio, categoria in ventas
]

# ==========================================
# LIST COMPREHENSION CON FILTRO
# ==========================================

productos_destacados = [
    producto
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 1000
]

# ==========================================
# DICT COMPREHENSION
# ==========================================

producto_info = {
    producto: {
        "valor": unidades * precio,
        "unidades": unidades
    }
    for producto, unidades, precio, categoria in ventas
}

# ==========================================
# DICT COMPREHENSION CON FILTRO
# ==========================================

ranking_premium = {
    producto: unidades * precio
    for producto, unidades, precio, categoria in ventas
    if precio > 50
}

ranking_premium = dict(
    sorted(
        ranking_premium.items(),
        key=lambda item: item[1],
        reverse=True
    )
)

# ==========================================
# SET COMPREHENSION
# ==========================================

categorias_unicas = {
    categoria
    for producto, unidades, precio, categoria in ventas
}

# ==========================================
# SET COMPREHENSION CON FILTRO
# ==========================================

productos_baratos = {
    producto
    for producto, unidades, precio, categoria in ventas
    if precio <= 50
}

# ==========================================
# RESUMEN FORMATEADO
# ==========================================

resumen_formateado = {
    producto: f"{unidades} unidades - ${unidades * precio}"
    for producto, unidades, precio, categoria in ventas
    if unidades * precio > 500
}

# ==========================================
# GRAN TOTAL
# ==========================================

gran_total = sum(valor_total)

# ==========================================
# REPORTE
# ==========================================

print("===== REPORTE DE VENTAS =====")

print("\nValor total por producto:")
print(valor_total)

print("\nProductos destacados:")
print(productos_destacados)

print("\nInformación de productos:")
print(producto_info)

print("\nRanking Premium:")
print(ranking_premium)

print("\nCategorías únicas:")
print(categorias_unicas)

print("\nProductos baratos:")
print(productos_baratos)

print("\nResumen formateado:")
print(resumen_formateado)

print(f"\nGran total de ventas: ${gran_total}")