# Tobacco and Cigarettes

## Tobacco

Tobacco is the base ingredient for Cigarettes and has it's own creating process.
First seed need to be made and grown, before the tobacco can be dried on a camp fire.

### Tobacco Seed

The Tobacco Seeds can be crafted like this:

{{ crafting(
    slots = [
        "A", "B", " ",
        " ", " ", " ",
        " ", " ", " "
    ],
    ingredients = {
        "A": {"name": "Wheat Seeds", "img": "wheat_seeds.png"},
        "B": {"name": "Leaf Litter", "img": "leaf_litter.png"}
    },
    result = {"name": "Tobacco Seed", "img": "tobacco_seed.png"}
) }}

You can use the seeds just like normal seeds in minecraft.

### Tobacco

Tobacco is the direkt result of growing the tobacco seeds, they look like this: ![tobacco](../assets/items/tobacco.png)

They have absolutly no other use than to make [**Dried Tobacco**](#dried-tobacco).

### Dried Tobacco

Can be made by putting the [Tobacco](#tobacco-1) on the campfire and waiting for a minute until it is dried.

It looks like this: ![dried_tobacco](../assets/items/dried_tobacco.png)

See [**Cigarettes**](#cigarettes) for what it can be used for.

## Cigarettes

Cigarettes are the actuall usefull item, tobacco is only used to make the ciarettes.
The item exists in multiple versions that have different abilities and desings.

### Cigarettes Item

This is the actuall Cigarette that can be crafted like this:

{{ crafting(
    slots = [
        "A", "A", "A",
        "B", "B", "B",
        "A", "A", "A"
    ],
    ingredients = {
        "A": {"name": "Paper", "img": "paper.png"},
        "B": {"name": "Dried Tobacco", "img": "dried_tobacco.png"}
    },
    result = {"name": "Cigarette", "img": "cigarette.png"}
) }}

If the item is in the main or offhand it can be used by right-clicking and the cigarette will be smoked.
The player will get some effects by smoking that don't hold long though.

In the future you maybe will be able to put the item on your head slot, so it looks like you are actually smoking
(Get on the nerves of one of the dev if that is something you want to have and it isn't yet implemented).

### 8 Cigarettes

This is just a crafting item needed for something else.

Crafting Recipe:

{{ crafting(
    slots = [
        "A", "A", "A",
        "A", "A", "A",
        "A", "A", " "
    ],
    ingredients = {
        "A": {"name": "Cigarette", "img": "cigarette.png"}
    },
    result = {"name": "8 Cigarettes", "img": "eight_cigarettes.png"}
) }}

### Cigarette Pack

This item has a cool design and holds 16 [Cigarettes](#cigarettes-item).
If you interact with the cigarette pack you will get 1 Cigarette and the pack takes 1 durability of damage (it has 16 obviously).

Crafting Recipe:

{{ crafting(
    slots = [
        "A", "B", "A",
        "A", "B", "A",
        "A", "A", "A"
    ],
    ingredients = {
        "A": {"name": "Paper", "img": "paper.png"},
        "B": {"name": "8 Cigarettes", "img": "eight_cigarettes.png"}
    },
    result = {"name": "Cigarette Pack", "img": "cigarette_pack.png"}
) }}
