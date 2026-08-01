# ======================================
# TIENDAS
# ======================================

tienda_centro = {"Mouse", "Teclado", "Monitor", "Impresora"}

tienda_norte = {"Monitor", "Teclado", "Audifonos", "Laptop"}

tienda_sur = {"Monitor", "Laptop", "Camara", "Teclado"}

# ======================================
# UNION
# ======================================

catalogo_completo = tienda_centro.union(
    tienda_norte,
    tienda_sur
)

# ======================================
# INTERSECTION
# ======================================

productos_comunes = tienda_centro.intersection(
    tienda_norte,
    tienda_sur
)

# ======================================
# EXCLUSIVOS
# ======================================

exclusivos_centro = tienda_centro.difference(
    tienda_norte.union(tienda_sur)
)

exclusivos_norte = tienda_norte.difference(
    tienda_centro.union(tienda_sur)
)

exclusivos_sur = tienda_sur.difference(
    tienda_centro.union(tienda_norte)
)

# ======================================
# ISDISJOINT
# ======================================

centro_norte = tienda_centro.isdisjoint(tienda_norte)

centro_sur = tienda_centro.isdisjoint(tienda_sur)

norte_sur = tienda_norte.isdisjoint(tienda_sur)

# ======================================
# USUARIOS
# ======================================

usuario1 = {"Accion", "Ciencia Ficcion", "Drama"}

usuario2 = {"Drama", "Comedia", "Accion"}

usuario3 = {"Terror", "Drama", "Accion"}

# ======================================
# OPERADORES
# ======================================

comunes = usuario1 & usuario2

universo = usuario1 | usuario2 | usuario3

exclusivos_usuario1 = usuario1 - usuario2

diferencias = usuario1 ^ usuario2

subconjunto = {"Drama", "Accion"} <= usuario1

# ======================================
# REPORTE
# ======================================

print("===== TIENDAS =====")

print("Catálogo completo:", catalogo_completo)

print("Productos comunes:", productos_comunes)

print("Exclusivos Centro:", exclusivos_centro)

print("Exclusivos Norte:", exclusivos_norte)

print("Exclusivos Sur:", exclusivos_sur)

print()

print("Centro y Norte sin coincidencias:", centro_norte)

print("Centro y Sur sin coincidencias:", centro_sur)

print("Norte y Sur sin coincidencias:", norte_sur)

print("\n===== PELÍCULAS =====")

print("Géneros comunes:", comunes)

print("Universo de géneros:", universo)

print("Exclusivos usuario1:", exclusivos_usuario1)

print("Diferencias simétricas:", diferencias)

print("¿Es subconjunto?:", subconjunto)