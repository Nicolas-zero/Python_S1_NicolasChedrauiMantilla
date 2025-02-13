from Abrirjson import abrir_JSON
def buscarEstudiante():
    estudiantes=abrir_JSON()
    try:
        id= int(input("Ingrese el ID "))
    except ValueError:
       print("INgrese algo bien , piense")
       return
    for estudiante in estudiantes.get("estudiantes","ni mrd hno"):
        if estudiante["id"]==id:
            print("Información del estudiante:")
            print(f"ID: {estudiante['id']}")
            print(f"Nombres: {estudiante['nombres']}")
            print(f"Apellidos: {estudiante['apellidos']}")
            print(f"Dirección: {estudiante['direccion']}")
            print(f"Acudiente: {estudiante['acudiente']}")
            print(f"Teléfono: {estudiante['telefono']}")
            print(f"nota: {estudiante['nota']}")
            print(f"nota1: {estudiante['nota1']}")
            print(f"nota2: {estudiante['nota2']}")
            print(f"nota_final: {estudiante['nota_final']}")
            print(f"salon: {estudiante['salon']}")
            
            print(f"Estado: {estudiante['estado']}")
            return
print("Estudiante no encontrado.")
from Abrirjson import abrir_JSON

