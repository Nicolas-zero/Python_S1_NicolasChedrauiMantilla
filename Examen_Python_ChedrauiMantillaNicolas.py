import json

def abrirJSON(registro_usuarios):
    dicFinal={}
    with open(f"./{registro_usuarios}.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("registro_usuarios.json",'w') as outFile:
        json.dump(dic,outFile)

Usuarios={}

Booleanito=True
while(Booleanito==True):

    print("==============================")
    print("    BIENVENIDO A MOVISTAR     ")
    print("==============================")
    print("¿que le gustaria hacer?")
    print("1. mirar informacion del cliente")
    print("2. seguiminto del historial")
    print("3. personalizar servicios")
    print("4. gestionar la fidelizacion")
    print("5. modulo de gestion de servicios")
    print("6. modulo de reporte")
    print("7. salir")
    opt=input(":")

    Usuarios=abrirJSON()
    if(opt=="1"):
        print(Usuarios)  
    elif(opt=="2"):
        print("Aqui esta el seguimiento del historial")
    elif(opt=="3"):
        print("¿desea personalizar un servicio? S/N")
        opt2=int(input(":"))
        if(opt2=="S"):
            print("personalize el servicio")
        else:
            exit 
    elif(opt=="4"):
        print("GESTION DE FIDELIZACION")
    elif(opt=="5"):
        print("MODULO DE GESTION DE SERVICIOS")
    elif(opt=="6"):
        print("MODULO DE REPORTES")
    else:
        break

#profesor, lo di todo pero aun se me complica el tema de los diccionarios, se como resorver el examen pero mi complicacion con los diccionarios es
#lo que me limito en esta ocasion, pido disculpas por entregarle esto asi y prometo comprometerme a mejorar mi manejo con los diccionarios
