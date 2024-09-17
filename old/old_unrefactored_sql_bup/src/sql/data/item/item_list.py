import sys
import sqlite3
import pandas as pd

from sql.generate.colour.colour_list import colour_list

from sql.generate.item.item_diet.item_diet_list import item_diet_list


from sql.generate.element.element_list import element_list

c = {color[0]: index+1 for index, color in enumerate(colour_list)}
i = {item_diet: index+1 for index, item_diet in enumerate(item_diet_list)}
e = {element[0]: index+1 for index, element in enumerate(element_list)}

item_list = [
    ("mead", i["alcohol"], c["yellow"], e["plant"], "a delicious, wine made from honey"),
    ("beer", i["alcohol"], c["yellow"], e["plant"], "an alcohol of hops and malt"),
    ("whiskey", i["alcohol"], c["brown"],e["plant"], "distilled beer"),
    ("vodka", i["alcohol"], c["silver"], e["plant"], "distilled neutral grain"),
    ("spider's legs", i["bug"], c["black"], e["evil"], "long, hairy legs to chew on"),
    ('butter', i["diary"], c["gold"], e["normal"], "creamy, salty and spreadable butter"),
    ("eggs", i["diary"], c["brown"], e["normal"], "protein capsules"),
    ("button mushroom", i["fungus"], c["white"], e["fungus"], "small, delicious mushrooms"),
    ("shiitake mushroom", i["fungus"], c["brown"], e["fungus"], "delicious rare mushrooms"),
    ("deathcap", i["fungus"], c["white"], e["fungus"], "A deadly poisonous mushrooms"),
    ("garnet", i["gemstone"], c["red"], e["normal"], "a silicate mineral"),
    ("emerald", i["gemstone"], c["green"], e["plant"], "a deep, green gemstone"),
    ("ruby", i["gemstone"], c["red"], e["fire"], "a deep, red gemstone"),
    ("diamond", i["gemstone"], c["silver"], e["holiness"], "a very rare, clear gemstone"),
    ("sapphire", i["gemstone"], c["blue"], e["water"], "a royal, purple stone"),
    ("quartz", i["gemstone"], c["silver"], e["water"], "a hard, silica stone"),
    ("steak", i["meat large"], c["brown"], e["normal"], "a delicious steak"),
    ("chops", i["meat large"], c["pink"], e["normal"], "some delicious chops"),
    ("hind legs", i["meat medium"], c["brown"], e["normal"], "the raggidy hind legs of a creature"),
    ("tail", i["meat medium"], c["black"], e["normal"], "the wiry tail of a creature"),
    ("head", i["meat small"], c["grey"], e["evil"], "a tiny head of a small creature" ),
    ("agave", i["plant hard root"], c["green"], e["plant"], "a root of an agave plant"),
    ("potato", i["plant soft root"], c["brown"], e["plant"], "an earthy root vegetable"),
    ("granite", i["rock"], c["dark grey"], e["earth"], "a hard rock"),
    ("mussel", i["shellfish"], c["pink"], e["water"], "a tasty shellfish"),
    ("cabbage", i["vegetable"], c["green"], e["plant"], "a tasty vegetable"),
    ("carrot", i["vegetable"], c["orange"], e["plant"], "a tasty vegetable"),
    ("rat", i["vermin"], c["dark grey"], e["poison"], "a horrible rat"),
    ("roadkill", i["vermin"], c["dark grey"], e["mutation"], "an old, crushed corpse"),
    ("birch", i["wood"], c["white"], e["plant"], "some white wood")
]
