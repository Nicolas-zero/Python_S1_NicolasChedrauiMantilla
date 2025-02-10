import json
import os

# Definimos el nombre del archivo JSON
DB_FILE = "Proyecto_Python.json"

# Función para abrir el archivo JSON y cargar los datos
def abrirJSON(ruta=""):
    dicFinal = {}
    try:
        # Creamos la ruta completa al archivo JSON, asegurándonos de combinar correctamente la ruta y el nombre del archivo
        archivo = os.path.join(ruta, DB_FILE)  # Si 'ruta' está vacía, se usa el archivo directamente en el directorio actual
        with open(archivo, 'r', encoding="utf-8") as openFile:
            dicFinal = json.load(openFile)
    except FileNotFoundError:
        print(f"El archivo {DB_FILE} no se encuentra.")
    except json.JSONDecodeError:
        print(f"Hubo un error al leer el archivo {DB_FILE}.")
    return dicFinal

# Función para mostrar los campers
def mostrar_campers():
    data = abrirJSON("")  # Llamamos a la función y le pasamos el nombre del archivo JSON (sin extensión)
    
    if "campers" in data:
        campers = data["campers"]
        print("==========================")
        print(" LISTA DE CAMPERS ")
        print("==========================")
        for camper in campers:
            print(f"ID: {camper['id']}")
            print(f"Nombre: {camper['nombres']} {camper['apellidos']}")
            print(f"Dirección: {camper['direccion']}")
            print(f"Acudiente: {camper['acudiente']}")
            print(f"Teléfono Celular: {camper['telefonos_contacto']['celular']}")
            print(f"Teléfono Fijo: {camper['telefonos_contacto']['fijo']}")
            print(f"Estado: {camper['estado']}")
            print(f"Riesgo: {camper['riesgo']}")
            print("==========================")
    else:
        print("No se encontraron campers en los datos.")

# Función para mostrar los trainers
def mostrar_trainers():
    data = abrirJSON("")  # Llamamos a la función y le pasamos el nombre del archivo JSON (sin extensión)
    
    if "trainer" in data:
        trainers = data["trainer"]
        print("==========================")
        print(" LISTA DE TRAINERS ")
        print("==========================")
        for trainer in trainers:
            print(f"ID: {trainer['id']}")
            print(f"Nombre: {trainer['nombre']} {trainer['apellidos']}")
            print(f"Grupo: {trainer['grupo']}")
            print("==========================")
    else:
        print("No se encontraron trainers en los datos.")

# Menú principal del programa
print("==========================")
print(" BIENVENIDO A CAMPUSLANDS ")
print("==========================")
username = input("Escribe tu usuario (Camper, Trainer, Coordinador): ")

usuarios_validos = ["Camper", "Trainer", "Coordinador"]
if username in usuarios_validos:
    print("Usuario válido, puedes continuar")
else:
    print("Usuario inválido")
    exit()  # Salir del programa si el usuario es inválido

# Funciones según el tipo de usuario
if username == "Camper":
    print("Bienvenido Camper")
    # Aquí irían las funciones del camper (por ejemplo, ver su estado, etc.)

elif username == "Trainer":
    print("Bienvenido Trainer")
    # Aquí puedes mostrar los trainers
    mostrar_trainers()  # Mostrar la lista de trainers cargada desde el archivo JSON

elif username == "Coordinador":
    print("Bienvenido Coordinador")
    print("¿Qué desea hacer?")
    print("1. Ver el registro de los campers")
    print("2. agregar Campers")
    print("3. eliminar Campers")
    print("4. agregar Trainer")
    print("5. eliminar Trainer")
    print("6. ver rutas")
    print("7. Crear una nueva ruta")
    print("8. elinimar una ruta")
    opcionC = int(input(":"))


    if opcionC == 1:
        mostrar_campers()  # Mostrar la lista de campers cargada desde el archivo JSON
    elif opcionC == 2:
        print("==========================")
        print("      AGREGAR CAMPER      ")
        print("==========================")
        # aca iria la logica para agregar campers
    elif opcionC == 3:
        print("==========================")
        print("     ELIMINAR CAMPER      ")
        print("==========================")
        # aca iria la logica apra eliminar campers
    elif opcionC == 4:
        print("==========================")
        print("      AGREGAR TRAINER     ")
        print("==========================")
        # aca iria la logica para agregar trainers
    elif opcionC == 5:
        print("==========================")
        print("      ELIMINAR TRAINER    ")
        print("==========================")
        # aca iria la logica para eliminar trainers
    elif opcionC == 6:
        print("==========================")
        print("           RUTAS          ")
        print("==========================")
        # Aquí iría la lógica para visualizar las rutas que hay 
    elif opcionC == 7:
        print("==========================")
        print("      AGREGAR RUTAS       ")
        print("==========================")
        # aca iria la logica para agregar rutas
    elif opcionC == 8:
        print("==========================")
        print("      ELIMINAR RUTAS      ")
        print("==========================")
        # aca iria la logica para eliminar rutas
    else:
        print("Opción inválida")
    

# Funciones para manejo de base de datos (json)

def cargar_datos():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {
        "campers": [],
        "trainers": [],
        "rutas_entrenamiento": [
            {"nombre": "NodeJS", "modulos": ["Fundamentos", "Web", "Formal", "DB", "Backend"]},
            {"nombre": "Java", "modulos": ["Fundamentos", "Web", "Formal", "DB", "Backend"]},
            {"nombre": "NetCore", "modulos": ["Fundamentos", "Web", "Formal", "DB", "Backend"]}
        ],
        "matriculas": [],
        "evaluaciones": []
    }

def guardar_datos(data):
    with open(DB_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

# Función para inscribir un camper
def inscribir_camper(camper):
    data = cargar_datos()
    data["campers"].append(camper)
    guardar_datos(data)

# Función para asignar campers aprobados a rutas
def asignar_camper_ruta(camper_id, ruta):
    data = cargar_datos()
    camper = next((c for c in data["campers"] if c["id"] == camper_id and c["estado"] == "Aprobado"), None)
    if camper:
        data["matriculas"].append({"camper_id": camper_id, "ruta": ruta})
        guardar_datos(data)
        return True
    return False

# Función para registrar notas
def registrar_nota(camper_id, nota_teorica, nota_practica, trabajos):
    nota_final = (nota_teorica * 0.3) + (nota_practica * 0.6) + (trabajos * 0.1)
    data = cargar_datos()
    data["evaluaciones"].append({"camper_id": camper_id, "nota_final": nota_final})
    guardar_datos(data)
    return nota_final >= 60

# Función para generar reportes
def generar_reporte():
    data = cargar_datos()
    return {
        "inscritos": [c for c in data["campers"] if c["estado"] == "Inscrito"],
        "aprobados": [c for c in data["campers"] if c["estado"] == "Aprobado"],
        "trainers": data["trainers"],
        "bajo_rendimiento": [e for e in data["evaluaciones"] if e["nota_final"] < 60],
    }

# Mensaje de confirmación al iniciar el sistema
if __name__ == "__main__":
    print("Sistema de seguimiento académico listo.")