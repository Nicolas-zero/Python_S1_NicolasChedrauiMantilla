from Abrirjson import abrir_JSON  

def ListaTrainer(trainers):
    
    
    
    
    if "trainers" in trainers and trainers["trainers"]:
        print("Lista de Trainers")
        print("ID/Nombres/Apellidos/Telefono/Horario")

    
        for trainers in trainers["trainers"]:
            
            valores = [
                str(trainers["id"]), 
                trainers["nombres"], 
                trainers["apellidos"], 
                trainers["telefono"], 
                trainers["horario"]
            ]
            
            
            print(" / ".join(valores))
    else:
        print("no hay estudiates en este grupo")
