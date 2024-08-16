import json

# Ouvrir le fichier JSON et le lire
with open('sampleJson.json', 'r') as f:
    data = json.load(f)

# Afficher les données
print("Page:", data['page'])
print("Per page:", data['per_page'])
print("Total:", data['total'])
print("Total pages:", data['total_pages'])

print("\nData:")
for item in data['data']:
    print(item)