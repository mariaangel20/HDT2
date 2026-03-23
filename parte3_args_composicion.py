# ============================================================
#  HDT2 — Parte 3: *args, **kwargs y Composición  (25 pts)
#  CineData GT 2026 — Sistema de Análisis de Cines
# ============================================================

# ============================================================
#  Ejercicio 3.1 — Funciones con *args  (8 pts)
# ============================================================
# a) Implementa `ingreso_total(*montos)` que reciba cualquier cantidad
#    de montos numéricos y RETORNE la suma de todos.
#    SIN usar sum(). Usa un ciclo for.
#
# b) Implementa `mejor_sala(*salas)` que reciba cualquier cantidad de
#    tuplas (nombre_sala, ventas). RETORNE la tupla con más ventas.
#    SIN usar max().
#    Si no recibe argumentos, retorna ("N/A", 0).
#
# c) Implementa `reporte_multisala(titulo, *funciones)` donde:
#    - titulo (str): título del reporte
#    - *funciones: cada argumento es una tupla (nombre, precio, vendidas, descuento)
#    Para cada función calcula:
#      ingreso = precio * vendidas * (1 - descuento/100)
#    RETORNA un string multilínea con el reporte y el total.
#    (Ver formato en salida esperada)

def ingreso_total(*montos):
    total = 0
    for monto in montos:
        total = total + monto
    return total


def mejor_sala(*salas):
    if not salas:
        return ("N/A", 0)
    mejor = salas[0]
    for sala in salas:
        if sala[1] > mejor[1]:
            mejor = sala
    return mejor


def reporte_multisala(titulo, *funciones):
    lineas = [f"=== {titulo} ==="]
    total = 0.0
    for i, (nombre, precio, vendidas, descuento) in enumerate(funciones, 1):
        ingreso = precio * vendidas * (1 - descuento / 100)
        total += ingreso
        lineas.append(f"Función {i}: {nombre:13s} | Q{ingreso:,.2f}")
    lineas.append("---")
    lineas.append(f"TOTAL: Q{total:,.2f}")
    return "\n".join(lineas)


# --- Pruebas (NO modificar) ---
print("=== Ejercicio 3.1 ===")
print(f"Ingreso total: Q{ingreso_total(1500.0, 2300.0, 800.0, 4100.0)}")
print(f"Ingreso vacío: Q{ingreso_total()}")

print(f"Mejor: {mejor_sala(('IMAX', 340), ('3D', 280), ('Kids', 180), ('Premium', 310))}")
print(f"Mejor vacío: {mejor_sala()}")

print()
print(reporte_multisala("Sala IMAX — Sábado",
                        ("Dune 2PM", 85.0, 150, 0),
                        ("Dune 5PM", 85.0, 200, 10),
                        ("Dune 8PM", 95.0, 180, 5)))

# Salida esperada:
# === Ejercicio 3.1 ===
# Ingreso total: Q8700.0
# Ingreso vacío: Q0
# Mejor: ('IMAX', 340)
# Mejor vacío: ('N/A', 0)
#
# === Sala IMAX — Sábado ===
# Función 1: Dune 2PM       | Q12750.00
# Función 2: Dune 5PM       | Q15300.00
# Función 3: Dune 8PM       | Q16245.00
# ---
# TOTAL: Q44295.00


# ============================================================
#  Ejercicio 3.2 — Funciones con **kwargs  (8 pts)
# ============================================================
# Implementa `ficha_pelicula(titulo, duracion, rating, **extras)` que
# RETORNE un string multilínea con la ficha de la película:
#
# Parámetros fijos: titulo, duracion (min), rating (float)
# **extras puede incluir: director, genero, año, idioma, pais, etc.
#
# Formato del string retornado:
# ┌──────────────────────────────┐
# │ TÍTULO                       │
# ├──────────────────────────────┤
# │ Duración: 175 min            │
# │ Rating  : ★ 8.7              │
# │ director: Villeneuve         │  ← Solo si hay extras
# │ genero  : Sci-Fi             │
# │ ...                          │
# └──────────────────────────────┘
#
# Ancho total del cuadro: 35 caracteres (contando bordes).
# El título va centrado. Las líneas de datos van alineadas a la izquierda.
# Cada clave de **extras se muestra capitalizada.

def ficha_pelicula(titulo, duracion, rating, **extras):
    ancho = 35
    lineas = []
    lineas.append("┌" + "─" * (ancho - 2) + "┐")
    
    # Título centrado
    titulo_formateado = titulo.center(ancho - 2)
    lineas.append("│" + titulo_formateado + "│")
    
    lineas.append("├" + "─" * (ancho - 2) + "┤")
    
    # Duración y Rating
    duracion_linea = f"Duración : {duracion} min".ljust(ancho - 2)
    lineas.append("│" + duracion_linea + "│")
    
    rating_linea = f"Rating   : ★ {rating}".ljust(ancho - 2)
    lineas.append("│" + rating_linea + "│")
    
    # Extras
    for clave, valor in extras.items():
        clave_capitalizada = clave.capitalize()
        linea = f"{clave_capitalizada} : {valor}".ljust(ancho - 2)
        lineas.append("│" + linea + "│")
    
    lineas.append("└" + "─" * (ancho - 2) + "┘")
    return "\n".join(lineas)


# --- Pruebas (NO modificar) ---
print("\n=== Ejercicio 3.2 ===")
print(ficha_pelicula("Dune: Parte 3", 175, 8.7,
                     director="Villeneuve", genero="Sci-Fi", año=2026))

print(ficha_pelicula("Inside Out 3", 105, 8.9))

# Salida esperada:
# === Ejercicio 3.2 ===
# ┌─────────────────────────────────┐
# │         Dune: Parte 3           │
# ├─────────────────────────────────┤
# │ Duración : 175 min              │
# │ Rating   : ★ 8.7                │
# │ Director : Villeneuve           │
# │ Genero   : Sci-Fi               │
# │ Año      : 2026                 │
# └─────────────────────────────────┘
# ┌─────────────────────────────────┐
# │          Inside Out 3           │
# ├─────────────────────────────────┤
# │ Duración : 105 min              │
# │ Rating   : ★ 8.9                │
# └─────────────────────────────────┘


# ============================================================
#  Ejercicio 3.3 — Composición de Funciones  (9 pts)
# ============================================================
# Aquí vas a construir un pipeline de análisis usando composición:
# cada función usa las anteriores como building blocks.
#
# a) `calcular_totales(ventas_por_sala)` — recibe un diccionario
#    {nombre_sala: [ventas_lun, ..., ventas_dom]}.
#    RETORNA una lista de tuplas [(nombre, total), ...].
#    Para sumar cada lista, usa `ingreso_total(*lista)` del ejercicio 3.1.
#
# b) `ordenar_salas(lista_tuplas)` — recibe una lista de tuplas (nombre, valor).
#    RETORNA una nueva lista ordenada de MAYOR a MENOR por valor.
#    Implementa ordenamiento burbuja. SIN usar sorted() ni .sort().
#
# c) `tendencia(valores)` — recibe una lista de números.
#    RETORNA: "ascendente" si cada valor >= anterior,
#             "descendente" si cada valor <= anterior,
#             "irregular" en otro caso.
#
# d) `reporte_semanal(nombre_cine, ventas_por_sala)` — función principal.
#    Usa calcular_totales, ordenar_salas, mejor_sala (3.1), y tendencia.
#    RETORNA un string con el reporte completo (ver formato abajo).
#    Para el promedio semanal de cada sala, divide total / 7.

def calcular_totales(ventas_por_sala):
    resultado = []
    for nombre_sala, ventas_lista in ventas_por_sala.items():
        total = ingreso_total(*ventas_lista)
        resultado.append((nombre_sala, total))
    return resultado


def ordenar_salas(lista_tuplas):
    # Hacer una copia para no modificar el original
    resultado = []
    for tupla in lista_tuplas:
        resultado.append(tupla)
    
    # Burbuja descendente
    for i in range(0, len(resultado)):
        for j in range(0, len(resultado) - 1 - i):
            if resultado[j][1] < resultado[j + 1][1]:
                # Intercambiar
                temp = resultado[j]
                resultado[j] = resultado[j + 1]
                resultado[j + 1] = temp
    
    return resultado


def tendencia(valores):
    if not valores or len(valores) < 2:
        return "irregular"
    
    es_ascendente = True
    es_descendente = True
    
    for i in range(1, len(valores)):
        if valores[i] < valores[i - 1]:
            es_ascendente = False
        if valores[i] > valores[i - 1]:
            es_descendente = False
    
    if es_ascendente:
        return "ascendente"
    elif es_descendente:
        return "descendente"
    else:
        return "irregular"


def reporte_semanal(nombre_cine, ventas_por_sala):
    # Calcular totales para cada sala
    totales = calcular_totales(ventas_por_sala)
    
    # Ordenar salas de mayor a menor
    salas_ordenadas = ordenar_salas(totales)
    
    # Construir reporte
    lineas = [f"=== REPORTE SEMANAL: {nombre_cine} ==="]
    
    for ranking, (nombre_sala, total) in enumerate(salas_ordenadas, 1):
        promedio = total / 7
        tend = tendencia(ventas_por_sala[nombre_sala])
        linea = f"#{ranking} {nombre_sala:12s} | Total: {total:4.0f} | Prom: {promedio:7.2f} | Tendencia: {tend}"
        lineas.append(linea)
    
    lineas.append("---")
    
    # Mejor sala de la semana
    mejor = mejor_sala(*totales)
    lineas.append(f"Mejor sala de la semana: {mejor[0]} ({mejor[1]:.0f} entradas)")
    
    return "\n".join(lineas)


# --- Pruebas (NO modificar) ---
print("\n=== Ejercicio 3.3 ===")

ventas = {
    "IMAX":     [120, 135, 140, 155, 200, 310, 280],
    "Sala 3D":  [200, 180, 160, 150, 140, 130, 110],
    "Kids":     [90, 95, 100, 105, 110, 115, 120],
    "Premium":  [100, 80, 95, 105, 170, 300, 250],
}

print(reporte_semanal("CineData Plaza", ventas))

# Salida esperada:
# === Ejercicio 3.3 ===
# === REPORTE SEMANAL: CineData Plaza ===
# #1 IMAX       | Total: 1340 | Prom: 191.43 | Tendencia: irregular
# #2 Premium    | Total: 1100 | Prom: 157.14 | Tendencia: irregular
# #3 Sala 3D    | Total: 1070 | Prom: 152.86 | Tendencia: descendente
# #4 Kids       | Total:  735 | Prom: 105.00 | Tendencia: ascendente
# ---
# Mejor sala de la semana: IMAX (1340 entradas)
