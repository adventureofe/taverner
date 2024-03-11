from sql.generate.colour.colour_main.colour import colour_list

c = {color[0]: index+1 for index, color in enumerate(colour_list)}


element_list = [
    ("alien", c["magenta"]),
    ("air", c["silver"]),
    ("chaos", c["orange"]),
    ("earth", c["brown"]),
    ("electricity", c["yellow"]),
    ("evil", c["black"]),
    ("fire", c["red"]),
    ("holiness", c["white"]),
    ("ice", c["cyan"]),
    ("metal", c["dark grey"]),
    ("mutation", c["maroon"]),
    ("normal", c["grey"]),
    ("plant", c["green"]),
    ("poison", c["purple"]),
    ("radiation", c["lime"]),
    ("undead", c["dark green"]),
    ("water", c["blue"])
]
