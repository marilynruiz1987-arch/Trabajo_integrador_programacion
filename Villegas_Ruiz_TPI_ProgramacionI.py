import os
import csv

def cargar_paises(nombre_archivo):
    paises = []
    try:
        with open(nombre_archivo, "r", encoding="latin-1") as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                if not fila["nombre"] or not fila["poblacion"] or not fila["superficie"] or not fila["continente"]:
                    print("Aviso: registro con campos vacíos ignorado")
                    continue
                try:
                    pais = {
                        "nombre": fila["nombre"],
                        "poblacion": int(fila["poblacion"]),
                        "superficie": int(fila["superficie"]),
                        "continente": fila["continente"]
                    }
                    paises.append(pais)
                except ValueError:
                    print(f"Aviso: error de formato en {fila['nombre']}")
    except FileNotFoundError:
        print(f"Error: No se encontró {nombre_archivo}")
    return paises

def agregar_pais(paises):
    nombre = input("Nombre del país: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return
    try:
        poblacion = int(input("Población: "))
        superficie = int(input("Superficie (km²): "))
    except ValueError:
        print("Error: población y superficie deben ser números.")
        return
    continente = input("Continente: ").strip()
    if continente == "":
        print("El continente no puede estar vacío.")
        return
    pais = {"nombre": nombre, "poblacion": poblacion, "superficie": superficie, "continente": continente}
    paises.append(pais)
    print("País agregado correctamente.")

def actualizar_pais(paises):
    nombre = input("Nombre del país a actualizar: ").strip().lower()
    for pais in paises:
        if pais["nombre"].lower() == nombre:
            try:
                pais["poblacion"] = int(input("Nueva población: "))
                pais["superficie"] = int(input("Nueva superficie (km²): "))
                print("País actualizado.")
            except ValueError:
                print("Error: valores deben ser números.")
            return
    print("País no encontrado.")

def buscar_pais(paises):
    texto = input("Buscar país por nombre: ").strip().lower()
    encontrados = False
    for pais in paises:
        if texto in pais["nombre"].lower():
            print(pais)
            encontrados = True
    if not encontrados:
        print("No se encontraron países.")

def filtrar_continente(paises):
    continente = input("Continente a filtrar: ").strip().lower()
    encontrados = False
    for pais in paises:
        if pais["continente"].lower() == continente:
            print(pais)
            encontrados = True
    if not encontrados:
        print("No se encontraron países en ese continente.")

def filtrar_poblacion(paises):
    try:
        minimo = int(input("Rango mínimo de población: "))
        maximo = int(input("Rango máximo de población: "))
    except ValueError:
        print("Error: rangos deben ser números.")
        return
    encontrados = False
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            print(pais)
            encontrados = True
    if not encontrados:
        print("No se encontraron países en ese rango de población.")

def filtrar_superficie(paises):
    try:
        minimo = int(input("Rango mínimo de superficie (km²): "))
        maximo = int(input("Rango máximo de superficie (km²): "))
    except ValueError:
        print("Error: rangos deben ser números.")
        return
    encontrados = False
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            print(pais)
            encontrados = True
    if not encontrados:
        print("No se encontraron países en ese rango de superficie.")

def ordenar_nombre(paises):
    ordenados = sorted(paises, key=lambda x: x["nombre"])
    for pais in ordenados:
        print(pais)

def ordenar_poblacion(paises):
    ordenados = sorted(paises, key=lambda x: x["poblacion"])
    for pais in ordenados:
        print(pais)

def ordenar_superficie(paises):
    opcion = input("Ordenar por superficie (A)scendente o (D)escendente: ").strip().upper()
    ordenados = sorted(paises, key=lambda x: x["superficie"], reverse=(opcion == "D"))
    for pais in ordenados:
        print(pais)

def estadisticas(paises):
    if len(paises) == 0:
        print("No hay países para calcular estadísticas.")
        return
    mayor = max(paises, key=lambda x: x["poblacion"])
    menor = min(paises, key=lambda x: x["poblacion"])
    promedio_poblacion = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_superficie = sum(p["superficie"] for p in paises) / len(paises)
    continentes = {}
    for pais in paises:
        continente = pais["continente"]
        if continente not in continentes:
            continentes[continente] = 0
        continentes[continente] += 1
    print(f"País con mayor población: {mayor['nombre']}")
    print(f"País con menor población: {menor['nombre']}")
    print(f"Promedio de población: {promedio_poblacion:.2f}")
    print(f"Promedio de superficie: {promedio_superficie:.2f}")
    print("Cantidad de países por continente:")
    for continente, cantidad in continentes.items():
        print(f"{continente}: {cantidad}")

def menu():
    paises = cargar_paises("paises.csv")
    while True:
        print("""
1 - Agregar país
2 - Actualizar país
3 - Buscar país
4 - Filtrar por continente
5 - Filtrar por población
6 - Filtrar por superficie
7 - Ordenar por nombre
8 - Ordenar por población
9 - Ordenar por superficie
10 - Estadísticas
0 - Salir
""")
        opcion = input("Opción: ").strip()
        if opcion == "1":
            agregar_pais(paises)
        elif opcion == "2":
            actualizar_pais(paises)
        elif opcion == "3":
            buscar_pais(paises)
        elif opcion == "4":
            filtrar_continente(paises)
        elif opcion == "5":
            filtrar_poblacion(paises)
        elif opcion == "6":
            filtrar_superficie(paises)
        elif opcion == "7":
            ordenar_nombre(paises)
        elif opcion == "8":
            ordenar_poblacion(paises)
        elif opcion == "9":
            ordenar_superficie(paises)
        elif opcion == "10":
            estadisticas(paises)
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu() 
    