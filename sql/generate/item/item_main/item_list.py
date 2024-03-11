import sys
import sqlite3
import pandas as pd

from sql.generate.colour.colour_main.colour import colour_list

from sql.generate.item.item_diet.item_diet_list import item_diet_list

c = {color[0]: index+1 for index, color in enumerate(colour_list)}
i = {item_diet: index+1 for index, item_diet in enumerate(item_diet_list)}

item_list = [
    ("mead", i["alcohol"], c["yellow"], "a delicious, wine made from honey"),
    ("beer", i["alcohol"], c["yellow"], "an alcohol of hops and malt"),
    ("whiskey", i["alcohol"], c["brown"], "distilled beer"),
    ("vodka", i["alcohol"], c["silver"], "distilled neutral grain"),
    ("centipede", i["bug"], c["brown"], "a long and meaty centipede"),
    ("spider's legs", i["bug"], c["black"], "long, hairy legs to chew on"),
    ('butter', i["diary"], c["gold"], "creamy, salty and spreadable butter"),
    ("eggs", i["diary"], c["brown"], "protein capsules"),
    ("button mushroom", i["fungus"], c["white"], "small, delicious mushrooms"),
    ("shiitake mushroom", i["fungus"], c["brown"], "delicious rare mushrooms"),
    ("deathcap", i["fungus"], c["white"], "A deadly poisonous mushrooms"),
    ("garnet", i["gemstone"], c["red"], "a silicate mineral"),
    ("emerald", i["gemstone"], c["green"], "a deep, green gemstone"),
    ("ruby", i["gemstone"], c["red"], "a deep, red gemstone"),
    ("diamond", i["gemstone"], c["silver"], "a very rare, clear gemstone"),
    ("amethyst", i["gemstone"], c["purple"], "a royal, purple stone"),
    ("quartz", i["gemstone"], c["silver"], "a hard, silica stone"),
    ("steak", i["meat large"], c["brown"], "a delicious steak"),
    ("chops", i["meat large"], c["pink"], "some delicious chops"),
    ("hind legs", i["meat medium"], c["brown"], "the raggidy hind legs of a creature"),
    ("tail", i["meat medium"], c["black"], "the wiry tail of a creature"),
    ("head", i["meat small"], c["grey"], "a tiny head of a small creature" ),
    ("agave", i["plant hard root"], c["green"], "a root of an agave plant"),
    ("potato", i["plant soft root"], c["brown"], "an earthy root vegetable"),
    ("granite", i["rock"], c["dark grey"], "a hard rock"),
    ("mussel", i["shellfish"], c["pink"], "a tasty shellfish"),
    ("cabbage", i["vegetable"], c["green"], "a tasty vegetable"),
    ("carrot", i["vegetable"], c["orange"], "a tasty vegetable"),
    ("rat", i["vermin"], c["dark grey"], "a horrible rat"),
    ("roadkill", i["vermin"], c["dark grey"], "an old, crushed corpse"),
    ("birch", i["wood"], c["white"], "some white wood")
]
