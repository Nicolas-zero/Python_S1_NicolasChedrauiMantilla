
from ModuloModificarEstudiante import *
from ModuloCrearEstudiante import CrearEstudiante
from Abrirjson import abrir_JSON
from Guardarjson import *
from ListaModulo import Lista
from MostrarCamper import buscarEstudiante
from EliminarEstudiante import eliminarEstudiante
from AgregarTrainer import CrearTrainer
from ListaTrainer import ListaTrainer
from EliminarTrainer import eliminarTrainer
from NotaCamper import nota
from CambiarEstado import estado
from AñadirSalon import CrearSalon
from CalcularNotaFinal import calcularNotaFinal
from CambiarNotaProyecto import NotaProyecto
from CambiarNotasTrabajo import NotaTrabajo
from actualizar_estado import actualizar_estado
from filtrar_estudiante import filtrar_estudiantes_salon

p=True
while p==True:
    estudiantes=abrir_JSON
    trainers=abrir_JSON
    print("1.Campers")
    print("2.Trainers")
    print("3.coordinacion")
    print("4. salir")
    b=input("Seleccione una opcion: ")
    if b=="1":
         
         print("1. Ver su informacion")
         print("2. Salir")
         a=input("Seleccione una opcion: ")
         if a=="1":
              buscarEstudiante()
         else:
              break
    if b=="2":
         print("1. mostrar estudiantes")
         print("2. ver estudiante en especifico")
         print("3. cambiar nota pruea inicial")
         print("4. cambiar nota trabajos")
         print("5. cambiar nota proyecto")
         print("6. ver nota final")
         print("7. Salir")
         
         c=input("Seleccione una opcion: ")
         if c=="1":
              Lista(estudiantes)
         elif c=="2":
              buscarEstudiante()
         elif c=="3":
              nota(estudiantes)
         elif c=="4":
              NotaTrabajo(estudiantes)
         elif c=="5":
              NotaProyecto(estudiantes)
         elif c=="6":
              calcularNotaFinal()
         else:
              break
estudiantes = abrir_JSON()  # Cargar el JSON
    trainers= abrir_JSON()
    print("\n--- Menú ---")
    print("1. Mostrar estudiantes")
    print("2. Agregar estudiante")   
    print("3. Modificar estudiante")
    print("4. ver a un estudiante(en especifico)")
    print("5. Eliminar estudiate")
    print("6. ver lista trainers")
    print("7. añadir trainer")
    print("8. eliminar Trainer")
    print("9. camnbiar nota prueba inicial")
    
    print("10. camibiar nota trabajos a algun camper")
    print("11. cambiar nota proyecto")
    print("12. ver nota final")
    p
    print("14. cambiar estado estudiante")

    print("15. añadir salon")

    print("16. salir")
    print("17. actualizar estado")
    print("18. mirar estudiantes segun el salon")
    opcion = input("Seleccione una opción: ")

    
    if opcion == "2":
            CrearEstudiante()
            
        
    elif opcion=="1":
        Lista(estudiantes)
    elif opcion=="2":
         CrearEstudiante()
    elif opcion=="3":
         ModificarEstudiantes(estudiantes)
         guardarJSON(estudiantes)
    elif opcion=="4":
         buscarEstudiante()
    elif opcion=="16":
         p=False###o break
    elif opcion=="5":
         eliminarEstudiante()
    elif opcion=="7":
         CrearTrainer()
    elif opcion=="6":
         ListaTrainer(trainers)
    elif opcion=="8":
         eliminarTrainer()
    elif opcion=="9":
         nota(estudiantes)
    elif opcion=="10":
         NotaTrabajo(estudiantes)
    elif opcion=="11":
         NotaProyecto(estudiantes)
         
    elif opcion=="12":
         calcularNotaFinal()
    elif opcion=="13":
         print()
         
    elif opcion=="14":
         estado(estudiantes)
    elif opcion=="15":
         CrearSalon()
    elif opcion=="17":
         actualizar_estado()
    elif opcion=="18":
         salon_id = input("Ingrese el ID del salón (A, B, C): ")
         
         
         
         
         
         
    else:
         print("mmmmm ya me daño el codigo")   
              
              
         
    
