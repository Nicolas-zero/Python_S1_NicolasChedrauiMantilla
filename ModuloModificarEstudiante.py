def ModificarEstudiantes(Lista_main):
    print("Modificar estudiante")
    try:
     id_estudiante= int(input("Ingresa el ID del estudiante que quieras cambiar"))
    except:
        print("error debe ingresar un Id correcto")
        return
        
    EstudianteEncontrar=None##none no es nada
    for estudiante in Lista_main["estudiantes"]:
        if estudiante["id"]==id_estudiante:
            EstudianteEncontrar=estudiante
            break
        
    if EstudianteEncontrar:
        print(f"Estudiante Encontrado: {EstudianteEncontrar['nombres']} {EstudianteEncontrar['apellidos']}")
        print("Ingresa los nuevos datos puedes presionar enter para dejar el actual : ")
        nombres=input(f"nombres:{EstudianteEncontrar ['nombres']}):"  or EstudianteEncontrar  ['nombres'])
        
        apellidos=input(f"apellidos:({EstudianteEncontrar ['apellidos']}):" ) or EstudianteEncontrar  ['apellidos']
        direccion=input(f"direccion:(({EstudianteEncontrar ['direccion']}):" ) or EstudianteEncontrar  ['direccion']
        acudiente=input(f"acudiente:({EstudianteEncontrar ['acudiente']}):" ) or EstudianteEncontrar  ['acudiente']
        telefono=input(f"telefono:({EstudianteEncontrar ['telefono']}):" ) or EstudianteEncontrar  ['telefono']
        estado=input(f"estado:({EstudianteEncontrar ['estado']}):" ) or EstudianteEncontrar  ['estado']
        salon=input(f"salon:({EstudianteEncontrar ['salon']}):" ) or EstudianteEncontrar  ['salon']
        
        nota=input(f"nota:({EstudianteEncontrar['nota']})")or EstudianteEncontrar['nota']
        EstudianteEncontrar["nombres"] = nombres
        EstudianteEncontrar["apellidos"] = apellidos
        EstudianteEncontrar["direccion"] = direccion
        EstudianteEncontrar["acudiente"] = acudiente
        EstudianteEncontrar["telefono"] = telefono
        EstudianteEncontrar["estado"] = estado
        EstudianteEncontrar["salon"]=salon
        
        print("estudiante datos modificados")
    else:
         print("estudiante no encontrado, escribalo bien")
