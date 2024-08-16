import json

# Supposons que le contenu JSON soit stocké dans un fichier appelé 'data.json'
filename = 'data.json'

# Ouvrir et lire le fichier JSON
with open('data.json', 'r') as file:
    data = json.load(file)

# Afficher le contenu du fichier JSON
print(json.dumps(data, indent=4))
