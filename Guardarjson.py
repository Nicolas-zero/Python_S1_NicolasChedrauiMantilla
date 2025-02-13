import json
def guardarJSON(dic):
    with open('./gghh.json', "w", encoding="utf-8") as outFile:
        json.dump(dic, outFile, indent=4)
    