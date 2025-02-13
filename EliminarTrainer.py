from Abrirjson import abrir_JSON
from Guardarjson import guardarJSON

def eliminarTrainer():
    trainer = abrir_JSON()
    try:
        id_trainer = int(input("Ingrese el ID del trainers que desea eliminar: "))
    except ValueError:
        print("Ingrese bien el ID ,piense")
        return

    trainers_encontrado = False
    for trainer_1 in trainer.get("trainers", []):
        if trainer_1["id"] == id_trainer:
            trainer["trainers"].remove(trainer_1)
            guardarJSON(trainer)
            estudiante_encontrado = True
            print(f"Trainer con ID {id_trainer} eliminado con éxito.")
            break

    if not trainers_encontrado:
        print("Digite bien el ID , PIENSE")