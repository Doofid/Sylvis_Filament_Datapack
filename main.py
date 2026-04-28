import os

def define_env(env):
    @env.macro
    def crafting(slots, ingredients, result):
        # 1. Berechne den Pfad zum Root-Verzeichnis (docs/)
        # env.variables.page.url gibt den Pfad der aktuellen Seite an
        page_url = env.variables.page.url
        depth = page_url.count('/')
        if page_url.endswith('/'): # Falls die URL auf / endet, eine Ebene abziehen
             depth -= 1
        
        # Erzeuge die passende Anzahl an "../"
        root_path = "../" * depth if depth > 0 else ""
        
        # 2. Setze den Pfad zu den Items fest (ausgehend von docs/)
        # Wenn deine Bilder in docs/assets/items liegen:
        img_base = f"{root_path}assets/items/"
        
        # HTML zusammenbauen
        html = '<div class="recipe-container" style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">'
        html += '<div class="mc-recipe">'
        
        for slot_key in slots:
            html += '<div class="mc-slot"'
            
            if slot_key.strip() and slot_key in ingredients:
                item = ingredients[slot_key]
                html += f' data-item-name="{item["name"]}">'
                html += f'<img src="{img_base}{item["img"]}" title="{item["name"]}">'
            else:
                html += '>' 
                
            html += '</div>'
            
        html += '</div>' 
        html += '<span style="font-size: 24px;">➜</span>'
        
        # Resultat
        html += f'<div class="mc-slot" style="width: 60px; height: 60px;" data-item-name="{result["name"]}">'
        html += f'<img src="{img_base}{result["img"]}" style="width: 48px; height: 48px;">'
        html += '</div></div>'
        
        return html