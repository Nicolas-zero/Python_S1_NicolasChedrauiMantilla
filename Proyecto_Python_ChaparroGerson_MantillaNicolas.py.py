import json
import os

# Función para abrir el archivo JSON y cargar los datos
def abrirJSON(Campers):
    dicFinal = {}
    archivo = f"./{Campers}.json"

    # Verificar si el archivo existe antes de intentar abrirlo
    if os.path.exists(archivo):
        try:
            with open(archivo, 'r') as openFile:
                dicFinal = json.load(openFile)
        except json.JSONDecodeError:
            print(f"Hubo un error al leer el archivo {Campers}.json. Asegúrate de que el formato JSON sea válido.")
        except Exception as e:
            print(f"Error al abrir el archivo {Campers}.json: {e}")
    else:
        print(f"El archivo {Campers}.json no se encuentra en el directorio.")
    
    return dicFinal

# Función para guardar datos en un archivo JSON
def guardarJSON(Campers, dic):
    try:
        with open(f"./{Campers}.json", 'w') as outFile:
            json.dump(dic, outFile, indent=4)
    except Exception as e:
        print(f"Error al guardar el archivo {Campers}.json: {e}")

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
    # Cargar la lista de campers desde el archivo Campers.json
    contenido = abrirJSON("Campers")
    
    if contenido:
        print(contenido)
    else:
        print("No se pudo cargar el archivo Campers.json")


elif username == "Trainer":
    print("Bienvenido Trainer")
    # Aquí puedes cargar y mostrar la lista de trainers desde el archivo Campers.json (o cualquier otra lógica)
    data = abrirJSON("Campers")
    if data:
        print("Lista de trainers:")
        for trainer in data.get("trainers", []):
            print(f"ID: {trainer['id']}, Nombre: {trainer['nombre']} {trainer['apellidos']}")
    else:
        print("No se encontraron trainers.")

elif username == "Coordinador":
    print("Bienvenido Coordinador")
    print("¿Qué desea hacer?")
    print("1. Ver el registro de los campers")
    print("2. Agregar Campers")
    print("3. Eliminar Campers")
    print("4. Agregar Trainer")
    print("5. Eliminar Trainer")
    print("6. Ver rutas")
    print("7. Crear una nueva ruta")
    print("8. Eliminar una ruta")
    opcionC = int(input(":"))

    data = abrirJSON("Campers")

    if opcionC == 1:
        if data:
            print("Lista de campers:")
            for camper in data.get("campers", []):
                print(f"ID: {camper['id']}, Nombre: {camper['nombres']} {camper['apellidos']}")
        else:
            print("No se encontraron campers.")
    
    elif opcionC == 2:
        print("==========================")
        print("      AGREGAR CAMPER      ")
        print("==========================")
        # Lógica para agregar campers (por ejemplo, solicitar los datos del nuevo camper)
        nuevo_camper = {
            "id": input("ID: "),
            "nombres": input("Nombres: "),
            "apellidos": input("Apellidos: "),
            "direccion": input("Dirección: "),
            "acudiente": input("Acudiente: "),
            "telefonos_contacto": {
                "celular": input("Teléfono Celular: "),
                "fijo": input("Teléfono Fijo: ")
            },
            "estado": input("Estado: "),
            "riesgo": input("Riesgo: ")
        }
        data["campers"].append(nuevo_camper)
        guardarJSON("Campers", data)
        print("Camper agregado correctamente.")

    elif opcionC == 3:
        print("==========================")
        print("     ELIMINAR CAMPER      ")
        print("==========================")
        # Lógica para eliminar un camper (por ejemplo, solicitar ID del camper a eliminar)
        camper_id = input("ID del camper a eliminar: ")
        data["campers"] = [camper for camper in data["campers"] if camper["id"] != camper_id]
        guardarJSON("Campers", data)
        print(f"Camper con ID {camper_id} eliminado.")

    elif opcionC == 4:
        print("==========================")
        print("      AGREGAR TRAINER     ")
        print("==========================")
        # Lógica para agregar trainers (similar a la de agregar campers)
        nuevo_trainer = {
            "id": input("ID: "),
            "nombre": input("Nombre: "),
            "apellidos": input("Apellidos: "),
            "grupo": input("Grupo: ")
        }
        data["trainers"].append(nuevo_trainer)
        guardarJSON("Campers", data)
        print("Trainer agregado correctamente.")

    elif opcionC == 5:
        print("==========================")
        print("      ELIMINAR TRAINER    ")
        print("==========================")
        # Lógica para eliminar un trainer
        trainer_id = input("ID del trainer a eliminar: ")
        data["trainers"] = [trainer for trainer in data["trainers"] if trainer["id"] != trainer_id]
        guardarJSON("Campers", data)
        print(f"Trainer con ID {trainer_id} eliminado.")

    elif opcionC == 6:
        print("==========================")
        print("           RUTAS          ")
        print("==========================")
        # Mostrar las rutas disponibles
        for ruta in data.get("rutas_entrenamiento", []):
            print(f"Ruta: {ruta['nombre']}, Módulos: {', '.join(ruta['modulos'])}")

    elif opcionC == 7:
        print("==========================")
        print("      AGREGAR RUTAS       ")
        print("==========================")
        # Lógica para agregar una nueva ruta
        nueva_ruta = {
            "nombre": input("Nombre de la ruta: "),
            "modulos": input("Modulos (separados por coma): ").split(',')
        }
        data["rutas_entrenamiento"].append(nueva_ruta)
        guardarJSON("Campers", data)
        print("Ruta agregada correctamente.")

    elif opcionC == 8:
        print("==========================")
        print("      ELIMINAR RUTAS      ")
        print("==========================")
        # Lógica para eliminar una ruta
        ruta_nombre = input("Nombre de la ruta a eliminar: ")
        data["rutas_entrenamiento"] = [ruta for ruta in data["rutas_entrenamiento"] if ruta["nombre"] != ruta_nombre]
        guardarJSON("Campers", data)
        print(f"Ruta {ruta_nombre} eliminada.")

    else:
        print("Opción inválida")
    

# Función para cargar los datos desde el archivo JSON
def cargar_datos():
    # Usamos la función abrirJSON para cargar los datos desde el archivo
    data = abrirJSON("Campers")  # Usamos el nombre del archivo sin la extensión .json
    if not data:  # Si no hay datos, devolver una estructura por defecto
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
    return data  # Si existen datos, los retornamos

# Función para guardar los datos en el archivo JSON
def guardar_datos(data):
    # Usamos la función guardarJSON para guardar los datos en el archivo
    guardarJSON("Campers", data)  # Usamos el nombre del archivo sin la extensión .json

# Mensaje de confirmación al iniciar el sistema
if __name__ == "__main__":
    print("Sistema de seguimiento académico listo.")

