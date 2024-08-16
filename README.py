import json

fichier_json = 'sampleJson.json'

fichier = fichier_json.read()

donnees = json.load(fichier)

print(donnees)
