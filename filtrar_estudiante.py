from Abrirjson import abrir_JSON

def filtrar_estudiantes_salon(salon_id):
    estudiantes = abrir_JSON().get("estudiantes", [])
    estudiantes_salon = [est for est in estudiantes if est["salon"] == salon_id]
    
    if estudiantes_salon:
        print(f"Estudiantes en el salón {salon_id}:")
        for est in estudiantes_salon:
            print(f"id: {est['id']}, Nombres: {est['nombres']}, Apellidos: {est['apellidos']}, nota Final: {est['nota_final']}, Estado: {est['estado']}")
    else:
        print(f"No hay estudiantes en el salón {salon_id}")
