from src.sql.colour_darkness.colour_darkness_list import colour_darkness_list
from src.sql.colour_base.colour_base_list import colour_base_list


d = {darkness[0]: index+1 for index, darkness in enumerate(colour_darkness_list)}
b = {base[0]: index+1 for index, base in enumerate(colour_base_list)}

colour_list =  [
    # name          r    g    b    darkness       base
    ('colourless',  255, 255, 255, d["transparent"], b["none"]),
    ('black',       0,     0,   0, d["black"],    b["grey"]),
    ('white',       255, 255, 255, d["white"],    b["grey"]),
    ('light grey',  192, 192, 192, d["light"],    b["grey"]),
    ('grey',        128, 128, 128, d["none"],     b["grey"]),
    ('dark grey',   64,   64,  64, d["dark"],     b["grey"]),
    ('light blue',  173, 216, 230, d["light"],    b["blue"]),
    ('blue',        0,     0, 255, d["none"],     b["blue"]),
    ('navy',        0,     0, 128, d["dark"],     b["blue"]),
    ('pink',        255, 182, 193, d["light"],    b["red"]),
    ('red',         255,   0,   0, d["none"],     b["red"]),
    ('maroon',      139,   0,   0, d["dark"],     b["red"]),
    ('light green', 144, 238, 144, d["light"],    b["green"]),
    ('green',       0,   128,   0, d["none"],     b["green"]),
    ('dark green',  0,   100,   0, d["dark"],     b["green"]),
    ('yellow',      255, 255,   0, d["none"],     b["yellow"]),
    ('dark yellow', 204, 204,   0, d["dark"],     b["yellow"]),
    ('lavender',    230, 230, 250, d["light"],    b["purple"]),
    ('purple',      128,   0, 128, d["none"],     b["purple"]),
    ('indigo',      75,    0, 130, d["dark"],     b["purple"]),
    ('peach',       255, 218, 185, d["light"],    b["orange"]),
    ('orange',      255, 165,   0, d["none"],     b["orange"]),
    ('dark orange', 255, 140,   0, d["dark"],     b["orange"]),
    ('tan',         210, 180, 140, d["light"],    b["brown"]),
    ('brown',       165,  42,  42, d["none"],     b["brown"]),
    ('dark brown',  101,  67,  33, d["dark"],     b["brown"]),
    ('cyan',        0,   255, 255, d["none"],     b["blue"]),
    ('lime',        96,  255,  96, d["light"],    b["green"]),
    ('magenta',     255,   0, 255, d["none"],     b["purple"]),
    ('silver',      192, 192, 192, d["metallic"], b["grey"]),
    ('gold',        239, 191,   4, d["metallic"], b["yellow"]),
    ('brass',       181, 166,  66, d["metallic"], b["brown"]),
    ('platinum',    229, 228, 226, d["metallic"], b["grey"]),
]
