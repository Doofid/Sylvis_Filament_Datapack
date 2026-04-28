def define_env(env):
    @env.macro
    def crafting(slots, ingredients, result):
        # Wir holen uns die base_url direkt aus der MkDocs-Konfiguration
        # Falls das nicht klappt, nutzen wir einen leeren String als Fallback
        base = env.conf.get('site_url', '')
        
        # Sicherere Methode für relative Pfade in MkDocs:
        # Wir nutzen die 'page'-Variable, um zu sehen, wo wir im Vergleich zum Root sind
        page = env.variables.page
        
        # Berechne den Pfad zurück zum Root
        # page.url ist z.B. 'tobacco/tobacco_main/'
        # Wir zählen die Slashes, um zu wissen, wie viele Ebenen wir hoch müssen
        url_parts = [p for p in page.url.split('/') if p]
        levels = len(url_parts)
        
        prefix = "../" * levels
        img_base = f"{prefix}assets/items/"

        html = '<div class="recipe-container" style="display: flex; align-items: center; gap: 20px; margin-bottom: 20px;">'
        html += '<div class="mc-recipe">'
        
        for slot_key in slots:
            key = slot_key.strip()
            html += '<div class="mc-slot"'
            
            if key and key in ingredients:
                item = ingredients[key]
                name = item.get("name", "Unknown Item")
                img = item.get("img", "test.png")
                
                html += f' data-item-name="{name}">'
                html += f'<img src="{img_base}{img}" title="{name}">'
            else:
                html += '>' 
            html += '</div>'
            
        html += '</div>'
        html += '<span style="font-size: 24px;">➜</span>'
        
        # Resultat
        res_name = result.get("name", "Unknown Result")
        res_img = result.get("img", "test.png")
        
        html += f'<div class="mc-slot" style="width: 60px; height: 60px;" data-item-name="{res_name}">'
        html += f'<img src="{img_base}{res_img}" style="width: 48px; height: 48px;">'
        html += '</div></div>'
        
        return html