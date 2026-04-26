import json
import os

# Konfiguration
source_folder = "stonecutter"
output_folder = "stonecutter_fixed"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def fix_recipe_structure(data):
    # Den alten String "#sylvis:sharks" korrigieren
    old_ingredient = data.get("ingredient", "")
    
    if isinstance(old_ingredient, str) and old_ingredient.startswith("#"):
        tag_name = old_ingredient.replace("#", "")
        # Die korrekte Struktur für 1.21.1 Fabric/Filament:
        data["ingredient"] = {
            "tag": tag_name
        }
    
    # Sicherstellen, dass das Resultat das moderne Format hat
    if "result" in data and isinstance(data["result"], dict):
        # 'item' wurde in neueren Versionen oft durch 'id' ersetzt
        if "item" in data["result"]:
            data["result"]["id"] = data["result"].pop("item")
            
    return data

# Durch den Ordner loopen
count = 0
for filename in os.listdir(source_folder):
    if filename.endswith(".json"):
        with open(os.path.join(source_folder, filename), 'r', encoding='utf-8') as f:
            try:
                recipe = json.load(f)
                fixed_recipe = fix_recipe_structure(recipe)
                
                with open(os.path.join(output_folder, filename), 'w', encoding='utf-8') as f:
                    json.dump(fixed_recipe, f, indent=2)
                count += 1
            except Exception as e:
                print(f"Fehler in {filename}: {e}")

print(f"Fertig! {count} Rezepte korrigiert in '{output_folder}' gespeichert.")
