import json
with open("Proyecto_Python.json","r") as Proyecto_json:
    camper= json.load(Proyecto_json)
print("==========================")
print(" BIENVENIDO A CAMPUSLANDS ")
print("==========================")
username=input(" escribe tu usuario (Camper, Trainer, Coordinador): ")
usuarios_validos=["Camper","Trainer","Coordinador"]
if username in usuarios_validos:
    print("Usuario valido, puedes continuar")
else:
    print("Usuario invalido")
    exit() #salir del programa si el usuario es invalido


if username == "Camper":
    print("Bienvenido Camper")
#falta añadir las funciones del camper
print(camper)

if username == "Trainer":
    print("Bienvenido Trainer")
#falta incluir las funciones del trainer


if username == "Coordinador":
    print("Bienvendio Coordinador")
    print("¿ Que desea hacer?")
    print("1. Ver el registro de los campers")
    print("2. Crear una nueva ruta")
    opcionC = int(input(":"))

    if (opcionC==1):
        #espacio reservado para el registro de notas de los campers:
        print("aca estan los registros de las notas de todos los campers")
        print("==========================")
        print(" REGISTRO DE LOS CAMPERS")
        print("==========================")
     
    if (opcionC==2):
        print("==========================")  
        print("           RUTAS          ")  
        print("==========================")  