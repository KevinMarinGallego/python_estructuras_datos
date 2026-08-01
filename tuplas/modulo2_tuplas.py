# ==================================
# CATÁLOGO DE PELÍCULAS
# ==================================

catalogo = (
    ("Titanic", "James Cameron", 1997, 9.5),
    ("Avatar", "James Cameron", 2009, 9.0),
    ("Inception", "Christopher Nolan", 2010, 9.4),
    ("Interstellar", "Christopher Nolan", 2014, 9.7)
)

# ==================================
# RECORRER EL CATÁLOGO
# ==================================

print("===== CATÁLOGO =====")

for titulo, director, anio, puntuacion in catalogo:
    print(f"Título: {titulo}")
    print(f"Director: {director}")
    print(f"Año: {anio}")
    print(f"Puntuación: {puntuacion}")
    print("----------------------")

# ==================================
# OPERADOR *
# ==================================

primera_pelicula, *resto = catalogo

print("\nPrimera película:")
print(primera_pelicula)

print("\nResto del catálogo:")
for pelicula in resto:
    print(pelicula)

# ==================================
# BUSCAR POR DIRECTOR
# ==================================

def buscar_por_director(director):

    coincidencias = []

    for pelicula in catalogo:

        if pelicula[1] == director:
            coincidencias.append(pelicula)

    return tuple(coincidencias)

# ==================================
# OBTENER ESTADÍSTICAS
# ==================================

def obtener_estadisticas(peliculas):

    puntuaciones = []

    for pelicula in peliculas:
        puntuaciones.append(pelicula[3])

    minima = min(puntuaciones)
    maxima = max(puntuaciones)
    promedio = sum(puntuaciones) / len(puntuaciones)

    return minima, maxima, promedio

# ==================================
# BUSCAR DIRECTOR
# ==================================

resultado = buscar_por_director("Christopher Nolan")

print("\nPelículas encontradas:")

for pelicula in resultado:
    print(pelicula)

# ==================================
# DESEMPAQUETAR ESTADÍSTICAS
# ==================================

minima, maxima, promedio = obtener_estadisticas(catalogo)

print("\n===== ESTADÍSTICAS =====")
print(f"Puntuación mínima: {minima}")
print(f"Puntuación máxima: {maxima}")
print(f"Promedio: {promedio}")