def define_env(env):
    @env.macro
    def crafting(slots, ingredients, result):
        # 1. Pfad-Präfix berechnen
        base = env.variables.base_url
        
        # Falls base ein Punkt ist oder leer, direkt assets ansteuern
        if not base or base == ".":
            prefix = ""
        else:
            # Sicherstellen, dass base mit einem Slash endet
            prefix = base if base.endswith("/") else f"{base}/"
            
        img_base = f"{prefix}assets/items/"

        html = '<div class="recipe-container" style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">'
        html += '<div class="mc-recipe">'
        
        # 2. Das 3x3 Gitter bauen
        for slot_key in slots:
            # Entferne Leerzeichen, um " " wie "" zu behandeln
            key = slot_key.strip()
            html += '<div class="mc-slot"'
            
            if key and key in ingredients:
                item = ingredients[key]
                name = item.get("name", "Unknown Item")
                img = item.get("img", "test.png")
                
                html += f' data-item-name="{name}">'
                html += f'<img src="{img_base}{img}" title="{name}">'
            else:
                html += '>' # Leerer Slot
            html += '</div>'
            
        html += '</div>' # Ende mc-recipe
        html += '<span style="font-size: 24px;">➜</span>'
        
        # 3. Das Resultat bauen
        res_name = result.get("name", "Unknown Result")
        res_img = result.get("img", "test.png")
        
        html += f'<div class="mc-slot" style="width: 60px; height: 60px;" data-item-name="{res_name}">'
        html += f'<img src="{img_base}{res_img}" style="width: 48px; height: 48px;">'
        html += '</div></div>'
        
        return html