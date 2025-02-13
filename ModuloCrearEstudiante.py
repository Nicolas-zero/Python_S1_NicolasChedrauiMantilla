from Guardarjson import guardarJSON
from Abrirjson import abrir_JSON



def CrearEstudiante():
    estudiantes = abrir_JSON()
    
    print("--- Crear Nuevo Estudiante ---")
    id = int(input("ID del estudiante: "))
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccion = input("Dirección: ")
    acudiente = input("Acudiente: ")
    telefono = input("Teléfono: ")
    salon=input("salon(A,B,C):")
    nota=input("nota")
    nota1=input("nota1")
    nota2=input("nota2")
    estado = input("Estado (En proceso de ingreso, Inscrito, Aprobado, Cursando, Graduado, Expulsado, Retirado): ")

    nuevo_estudiante = {
        "id": id,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefono": telefono,
        "salon": salon,
        "nota":nota,
        "nota1":nota1,
        "nota2":nota2,
        "estado": estado
    }
    
    estudiantes["estudiantes"].append(nuevo_estudiante)
    guardarJSON(estudiantes)
    return nuevo_estudiante
