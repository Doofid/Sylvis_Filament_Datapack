# Dokumentations-Titel (H1)

Dies ist ein normaler Textabsatz mit **fetten Wörtern**, *kursiven Hervorhebungen* und sogar ~~durchgestrichenem Text~~. Du kannst auch [Links zu anderen Seiten](index.md) oder zu [externen Webseiten](https://google.com) einfügen.

---

## Überschrift Ebene 2 (H2)

Hier siehst du, wie Listen funktionieren:

* Erster Punkt einer ungeordneten Liste
* Zweiter Punkt
    * Ein eingerückter Unterpunkt
* Dritter Punkt

### Unterüberschrift Ebene 3 (H3)

Falls du eine Schritt-für-Schritt-Anleitung brauchst:

1.  Erster geordneter Schritt
2.  Zweiter geordneter Schritt
3.  Dritter geordneter Schritt

---

## Code und Befehle

Wenn du Minecraft-Befehle im Text erwähnst, nutzt du `Inline Code`.

Für ganze Dateien oder Datapack-Logik nutzt du Code-Blöcke mit Sprachangabe:

```json
{
  "pool": {
    "rolls": 1,
    "entries": [
      {
        "type": "item",
        "name": "minecraft:diamond"
      }
    ]
  }
}
```

---

## Tabellen für Item-Stats

| Item-Name | Angriffsschaden | Geschwindigkeit | Seltenheit |
| :--- | :---: | :---: | ---: |
| Shark Sword | 7.0 | 1.6 | **Epic** |
| Jester Hat | 1.0 | 2.0 | Common |
| Tobacco Pipe | 0.5 | 1.0 | Rare |

> **Hinweis (Blockquote):**
> Dies ist ein klassisches Zitat oder eine einfache Notiz.
> Es kann über mehrere Zeilen gehen, solange jede Zeile mit einem ">" beginnt.

---

## Bilder und Medien

Hier wird ein Bild aus deinem Assets-Ordner eingebunden:
![Alternativtext für das Bild](assets/items/blue_shark.png)

---

## Checklisten (To-Dos)

- [x] Grundgerüst des Wikis erstellt
- [x] Erste Rezepte hinzugefügt
- [ ] Bilder für alle Haie hochladen
- [ ] Tobacco-System dokumentieren

---

## Spezialitäten

### Fußnoten
Hier ist eine Aussage, die eine genauere Erklärung benötigt[^1].

### Zeilenumbrüche
Erste Zeile  
Zweite Zeile (durch zwei Leerzeichen am Ende der ersten Zeile erzwungen)

---

### Ein paar Tipps zum Kopieren:
1. **Trennlinien:** Das `---` erzeugt eine horizontale Linie, die super ist, um verschiedene Items auf einer Seite optisch zu trennen.
2. **Tabellen-Ausrichtung:** In der Tabellen-Zeile unter den Headern bestimmt der Doppelpunkt die Ausrichtung:
    - `:---` = linksbündig
    - `:---:` = zentriert
    - `---:` = rechtsbündig
3. **Leerzeilen:** Achte darauf, vor und nach Listen, Tabellen und Code-Blöcken immer eine komplette Leerzeile zu lassen, damit MkDocs sie fehlerfrei erkennt.

---

[^1]: Dies ist die Erklärung der Fußnote, die am Ende der Seite erscheint.
