nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]

print("Nombres:", nombres)
print("Apellidos:", apellidos)

booleanito = True
#opciones que se van  mostrar cuando se inicie el prorama
while (booleanito==True):
    print("\nBienvenido al programa de lista de estudiantes")
    print("segun las opcioones que el program tiene usted puede editar la lista a su gusto")
    print("1) Agregar estudiante")
    print("2) Ver estudiantes")
    print("3) Editar estudiante")
    print("4) Eliminar estudiante")
    print("5) salir del programa")
opcionusuario= int(input(":"))
#opcion 2/ visualizar la lista de los estudiantes
if(opcionusuario==2):
    print("Lista de los estudiantes de la sede cajasan:")
    for i in range (len(nombres)):
     print("Estudiante #" ,i+1,": ", nombres, apellidos[i])
#opcion 5/ finalizar el programa  
elif(opcionusuario==5):
   booleanito=False
   break
#opcion 1/ agregar estudiantes
elif(opcionusuario==3):
        print("Lista de estudiantes:")
        for i in range(len(nombres)):
            print("Estudiante #",i+1,": ",nombres,apellidos[i])
        numeroEstudiante=int(input("Cual estudiante quieres editar?:"))
        nombreEstudianteNuevo=input("Cual será el nombre nuevo del estudiante?:")
        nombres[numeroEstudiante-1]=nombreEstudianteNuevo
#opcion 4/ eliminar estudiantes
elif(opcionusuario==4):
        print("Lista de estudiantes:")
        for i in range(len(nombres)):
            print("Estudiante #",i+1,": ",nombres,apellidos[i])
        numeroEstudiante=int(input("Cual estudiante quieres eliminar?:"))
        nombres.pop(numeroEstudiante-1)