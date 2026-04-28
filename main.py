# main.py
def define_env(env):
    @env.macro
    def crafting(slots, ingredients, result):
        # Basis-Pfad zu deinen Bildern
        img_path = "../assets/items/"
        
        html = '<div class="recipe-container" style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">'
        html += '<div class="mc-recipe">'
        
        for slot_key in slots:
            html += '<div class="mc-slot"'
            
            # Wenn der Slot nicht leer ist und in ingredients existiert
            if slot_key.strip() and slot_key in ingredients:
                item = ingredients[slot_key]
                html += f' data-item-name="{item["name"]}">'
                html += f'<img src="{img_path}{item["img"]}" title="{item["name"]}">'
            else:
                html += '>' # Leerer Slot
                
            html += '</div>'
            
        html += '</div>' # Ende mc-recipe
        html += '<span style="font-size: 24px;">➜</span>'
        
        # Resultat
        html += f'<div class="mc-slot" style="width: 60px; height: 60px;" data-item-name="{result["name"]}">'
        html += f'<img src="{img_path}{result["img"]}" style="width: 48px; height: 48px;">'
        html += '</div></div>'
        
        return html
