# Cat Ears

## Choose the correct one

There exists two versions of the cat ears.
One is a tiny bit bigger than the other one and with the main difference that it is positioned a pixel higher on the head.
The reason for that is, that depending on the skin a player has, the head may have an outer layer or only an inner layer.
Those two layers are not on the same height and make the head a bit bigger.
So if you want to make the cat ears look correct on yourself, choose the correct version.

## Crafting

### Cat Ears Low

{{ crafting(
    slots = [
        "", "", "",
        "D", "", "D",
        "E", "", "E"
    ],
    ingredients = {
        "D": {"name": "White Wool", "img": "White_Wool.png"},
        "E": {"name": "Pink Wool", "img": "Pink_Wool.png"}
    },
    result = {"name": "Cat Ears Low", "img": "Cat_Ears_Skin.png"}
) }}

### Cat Ears High

{{ crafting(
    slots = [
        "A", "", "A",
        "D", "", "D",
        "E", "", "E"
    ],
    ingredients = {
        "A": {"name": "White Wool", "img": "White_Wool.png"},
        "D": {"name": "Pink Wool", "img": "Pink_Wool.png"},
        "E": {"name": "Stick", "img": "stick.png"}
    },
    result = {"name": "Cat Ears Low", "img": "Cat_Ears_Skin.png"}
) }}

