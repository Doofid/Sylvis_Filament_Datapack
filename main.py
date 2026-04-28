def define_env(env):
    @env.macro
    def crafting(slots, ingredients, result):
        # 'base_url' ist eine MkDocs-Variable, die immer den 
        # korrekten relativen Pfad zum Root-Ordner (docs/) enthält.
        base = env.variables.base_url
        
        # Falls base leer ist (auf der Startseite), brauchen wir keinen Slash
        prefix = f"{base}/" if base else ""
        img_base = f"{prefix}assets/items/"

        html = '<div class="recipe-container" style="display: flex; align-items: center; gap: 20px;">'
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
            
        html += '</div><span style="font-size: 24px;">➜</span>'
        
        # Resultat
        html += f'<div class="mc-slot" style="width: 60px; height: 60px;" data-item-name="{result["name"]}">'
        html += f'<img src="{img_base}{result["img"]}" style="width: 48px; height: 48px;">'
        html += '</div></div>'
        
        return html