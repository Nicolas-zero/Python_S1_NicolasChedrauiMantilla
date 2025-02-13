from Abrirjson import abrir_JSON
from Guardarjson import guardarJSON

def eliminarEstudiante():
    estudiantes = abrir_JSON()
    try:
        id_estudiante = int(input("Ingrese el ID del estudiante que desea eliminar: "))
    except ValueError:
        print("Ingrese bien el ID ,piense")
        return

    estudiante_encontrado = False
    for estudiante in estudiantes.get("estudiantes", []):
        if estudiante["id"] == id_estudiante:
            estudiantes["estudiantes"].remove(estudiante)
            guardarJSON(estudiantes)
            estudiante_encontrado = True
            print(f"Estudiante con ID {id_estudiante} eliminado con éxito.")
            break

    if not estudiante_encontrado:
        print("Digite bien el ID , PIENSE")