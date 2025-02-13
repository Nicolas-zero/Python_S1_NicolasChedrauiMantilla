import json
def abrir_JSON():
    with open("./gghh.json") as openFile:
        dicFinal=json.load(openFile)
    return dicFinal