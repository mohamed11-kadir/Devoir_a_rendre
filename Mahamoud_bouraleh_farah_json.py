import json


def fichier_json(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        data = json.load(fichier)
    return data


nom_fichier = 'sampleJson (1).json'
donnees = fichier_json(nom_fichier)


print(donnees)
