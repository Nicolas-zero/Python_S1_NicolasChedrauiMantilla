from Guardarjson import guardarJSON
def nota(Lista_main):
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
        nota=int(input(f"nota actual(Prueba inicial):({EstudianteEncontrar ['nota']}):") ) or EstudianteEncontrar  ['nota']
        EstudianteEncontrar["nota"]= nota
        guardarJSON(Lista_main)

        print("nota modificada")
    
    else:
        print("escriba bien")
