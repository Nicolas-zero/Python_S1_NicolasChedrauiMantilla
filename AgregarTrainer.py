from Guardarjson import guardarJSON
from Abrirjson import abrir_JSON



def CrearTrainer():
    trainers = abrir_JSON()
    
    print("--- Crear Nuevo Estudiante ---")
    id = int(input("ID del estudiante: "))
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono = input("Teléfono: ")
    horario = input("Horario(Full Time//6am-2pm//2pm-10pm): ")

    nuevo_trainers = {
        "id": id,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "horario": horario
    }
    
    trainers["trainers"].append(nuevo_trainers)
    guardarJSON(trainers)
    return nuevo_trainers