from Guardarjson import guardarJSON
def NotaProyecto(Lista_main):
    print("Modificar estudiante")
    try:
     id_estudiante= int(input("Ingresa el ID del estudiante que quieras cambiar la nota"))
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
        nota1=int(input(f"nota actual(Proyecto):({EstudianteEncontrar ['nota1']}):") ) or EstudianteEncontrar  ['nota1']
        EstudianteEncontrar["nota1"]= nota1
        guardarJSON(Lista_main)

        print("nota modificada")
    
    else:
        print("escriba bien")
