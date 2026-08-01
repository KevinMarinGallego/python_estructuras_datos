# =====================================
# VENTAS POR REGIÓN
# =====================================

ventas_por_region = {
    "Norte": {
        "Q1": 15000,
        "Q2": 18000,
        "Q3": 17000,
        "Q4": 20000
    },
    "Centro": {
        "Q1": 22000,
        "Q2": 21000,
        "Q3": 25000,
        "Q4": 24000
    },
    "Sur": {
        "Q1": 12000,
        "Q2": 14000,
        "Q3": 16000,
        "Q4": 15000
    }
}

# =====================================
# CALCULAR TOTALES POR REGIÓN
# =====================================

totales_region = {}

for region, ventas in ventas_por_region.items():
    totales_region[region] = sum(ventas.values())

# =====================================
# REGIÓN CON MAYORES VENTAS
# =====================================

mejor_region = max(totales_region, key=lambda region: totales_region[region])

# =====================================
# TOTALES POR TRIMESTRE
# =====================================

totales_por_trimestre = {
    "Q1": 0,
    "Q2": 0,
    "Q3": 0,
    "Q4": 0
}

for region, ventas in ventas_por_region.items():
    for trimestre, valor in ventas.items():
        totales_por_trimestre[trimestre] += valor

# =====================================
# GRAN TOTAL
# =====================================

gran_total = sum(totales_region.values())

# =====================================
# PORCENTAJES
# =====================================

porcentajes = {
    region: (total / gran_total) * 100
    for region, total in totales_region.items()
}

# =====================================
# REPORTE ORDENADO
# =====================================

print("===== REPORTE DE VENTAS =====\n")

print(f"Región con mayores ventas: {mejor_region}\n")

print("Ventas por región:")

for region, total in sorted(
    totales_region.items(),
    key=lambda item: item[1],
    reverse=True
):
    print(f"{region}: ${total} ({porcentajes[region]:.2f}%)")

print("\nVentas por trimestre:")

for trimestre, total in totales_por_trimestre.items():
    print(f"{trimestre}: ${total}")

print(f"\nGran total anual: ${gran_total}")