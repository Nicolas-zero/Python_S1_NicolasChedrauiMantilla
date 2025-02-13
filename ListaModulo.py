from Abrirjson import abrir_JSON

def Lista(estudiantes):
    if "estudiantes" in estudiantes and estudiantes["estudiantes"]:
        print("Lista de estudiantes")
        print("ID/Nombres/Apellidos/Direccion/Acudiente/Telefono/Estado")

        for estudiante in estudiantes["estudiantes"]:
            valores = [
                str(estudiante["id"]),
                estudiante["nombres"],
                estudiante["apellidos"],
                estudiante["direccion"],
                estudiante["acudiente"],
                estudiante["telefono"],
                estudiante["estado"]
            ]
            print(" / ".join(valores))
    else:
        print("No hay estudiantes en este grupo")

if __name__ == "__main__":
    data = abrir_JSON()
    Lista(data)