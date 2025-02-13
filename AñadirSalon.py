from Guardarjson import guardarJSON
from Abrirjson import abrir_JSON

def CrearSalon():
    data = abrir_JSON()
    
    print("--- Crear Nuevo Salon ---")
    id = input("ID del salon: ")
    nombre = input("Nombre del salon: ")

    nuevo_salon = {
        "id": id,
        "nombre": nombre
    }
    
    data["salones"].append(nuevo_salon)
    guardarJSON(data)
    return nuevo_salon