import random
from Abrirjson import abrir_JSON
from Guardarjson import guardarJSON

def actualizar_estado():
    data = abrir_JSON()
    rutas = data["rutas"]
    salones = data["salones"]

    for estudiante in data["estudiantes"]:
        if estudiante["nota_final"] > 59:
            estudiante["estado"] = "aprobado"
            estudiante["ruta"] = random.choice(rutas)["ruta"]
            estudiante["salon"] = random.choice(salones)["id"]
        else:
            estudiante["estado"] = "desaprobado"
            estudiante["ruta"] = ""
            estudiante["salon"] = ""

    guardarJSON(data)
    print("Estado de los estudiantes actualizado y rutas asignadas a los aprobados.")