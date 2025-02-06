import json

# Lista inicial de inmuebles
inmuebles = [
    {'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
    {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
    {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
    {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
    {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}
]

def calcular_precio(inmueble):
    antiguedad = 2025 - inmueble['año']
    base = inmueble['metros'] * 1000 + inmueble['habitaciones'] * 5000 + (15000 if inmueble['garaje'] else 0)
    if inmueble['zona'] == 'A':
        precio = base * (1 - antiguedad / 100)
    elif inmueble['zona'] == 'B':
        precio = base * (1 - antiguedad / 100) * 1.5
    return round(precio, 2)

def buscar_por_presupuesto(inmuebles, presupuesto):
    resultado = []
    for inmueble in inmuebles:
        precio = calcular_precio(inmueble)
        if precio <= presupuesto:
            inmueble_con_precio = inmueble.copy()
            inmueble_con_precio['precio'] = precio
            resultado.append(inmueble_con_precio)
    return resultado

def mostrar_inmuebles(inmuebles):
    for i, inmueble in enumerate(inmuebles):
        print(f"[{i}] {inmueble}")

def agregar_inmueble(inmuebles):
    try:
        año = int(input("Año de construcción: "))
        metros = int(input("Metros cuadrados: "))
        habitaciones = int(input("Número de habitaciones: "))
        garaje = input("¿Tiene garaje? (s/n): ").strip().lower() == 's'
        zona = input("Zona (A/B): ").strip().upper()
        if zona not in ['A', 'B']:
            raise ValueError("Zona no válida")
        inmuebles.append({'año': año, 'metros': metros, 'habitaciones': habitaciones, 'garaje': garaje, 'zona': zona})
        print("Inmueble agregado correctamente.")
    except Exception as e:
        print(f"Error al agregar inmueble: {e}")

def actualizar_inmueble(inmuebles):
    try:
        mostrar_inmuebles(inmuebles)
        index = int(input("Seleccione el índice del inmueble a actualizar: "))
        if 0 <= index < len(inmuebles):
            inmueble = inmuebles[index]
            print("Deje en blanco para no modificar un atributo.")
            año = input(f"Año de construcción ({inmueble['año']}): ")
            metros = input(f"Metros cuadrados ({inmueble['metros']}): ")
            habitaciones = input(f"Número de habitaciones ({inmueble['habitaciones']}): ")
            garaje = input(f"¿Tiene garaje? ({'s' if inmueble['garaje'] else 'n'}): ").strip().lower()
            zona = input(f"Zona ({inmueble['zona']}): ").strip().upper()

            if año:
                inmueble['año'] = int(año)
            if metros:
                inmueble['metros'] = int(metros)
            if habitaciones:
                inmueble['habitaciones'] = int(habitaciones)
            if garaje in ['s', 'n']:
                inmueble['garaje'] = garaje == 's'
            if zona in ['A', 'B']:
                inmueble['zona'] = zona

            print("Inmueble actualizado correctamente.")
        else:
            print("Índice no válido.")
    except Exception as e:
        print(f"Error al actualizar inmueble: {e}")

def eliminar_inmueble(inmuebles):
    try:
        mostrar_inmuebles(inmuebles)
        index = int(input("Seleccione el índice del inmueble a eliminar: "))
        if 0 <= index < len(inmuebles):
            inmuebles.pop(index)
            print("Inmueble eliminado correctamente.")
        else:
            print("Índice no válido.")
    except Exception as e:
        print(f"Error al eliminar inmueble: {e}")

def guardar_datos(inmuebles):
    with open("inmuebles.json", "w") as archivo:
        json.dump(inmuebles, archivo)
    print("Datos guardados correctamente.")

def cargar_datos():
    try:
        with open("inmuebles.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("No se encontró un archivo previo. Se usará la lista inicial.")
        return inmuebles

def menu():
    inmuebles = cargar_datos()
    while True:
        print("\nMenú:")
        print("1. Buscar inmuebles por presupuesto")
        print("2. Agregar inmueble")
        print("3. Actualizar inmueble")
        print("4. Eliminar inmueble")
        print("5. Mostrar todos los inmuebles")
        print("6. Guardar y salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            try:
                presupuesto = float(input("Ingrese el presupuesto: "))
                resultado = buscar_por_presupuesto(inmuebles, presupuesto)
                print("Inmuebles encontrados:")
                mostrar_inmuebles(resultado)
            except ValueError:
                print("Presupuesto no válido.")
        elif opcion == '2':
            agregar_inmueble(inmuebles)
        elif opcion == '3':
            actualizar_inmueble(inmuebles)
        elif opcion == '4':
            eliminar_inmueble(inmuebles)
        elif opcion == '5':
            mostrar_inmuebles(inmuebles)
        elif opcion == '6':
            guardar_datos(inmuebles)
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()