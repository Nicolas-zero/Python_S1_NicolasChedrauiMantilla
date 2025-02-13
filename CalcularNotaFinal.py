from Guardarjson import guardarJSON
from Abrirjson import abrir_JSON

def calcularNotaFinal():
    data = abrir_JSON()
    estudiantes = data.get("estudiantes", [])

    try:
     id_estudiante= int(input("Ingresa el ID del estudiante que quieras cambiar la nota"))
    except:
        print("error debe ingresar un Id correcto")
        return
        

    for estudiante in estudiantes:
        if estudiante.get("id") == id_estudiante:
            nota = estudiante.get("nota", 0)
            nota1 = estudiante.get("nota1", 0)
            nota2 = estudiante.get("nota2", 0)

            nota_final = (nota * 0.30) + (nota1 * 0.60) + (nota2 * 0.10)
            estudiante["nota_final"] = nota_final

            print(f"Nota final del estudiante con ID {id_estudiante}: {nota_final}")
            estudiante_encontrado = True
            break

    if not estudiante_encontrado:
        print(f"No se encontró el estudiante con ID {id_estudiante}")

    guardarJSON(data)