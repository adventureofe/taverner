from src.sql.colour_darkness.colour_darkness_list import colour_darkness_list
from src.sql.colour_base.colour_base_list import colour_base_list

cd = {colour_darkness[0]: index+1 for index, colour_darkness in enumerate(colour_darkness_list)}
cb = {colour_base[0]: index+1 for index, colour_base in enumerate(colour_base_list)}

colour_list =  [
    # name          r    g    b
    ('colourless', 255, 255, 255, cd["transparent"], cb["none"]),

    ('black',      0,     0,   0, cd["black"], cb["grey"]),
    ('white',      255, 255, 255, cd["white"], cb["grey"]),

    ('light grey', 192,  192, 192, cd["light"], cb["grey"]),
    ('grey',       128, 128, 128, cd["none"], cb["grey"]),
    ('dark grey',  64,   64,   64, cd["dark"], cb["grey"]),

    ('light blue', 173, 216, 230, cd["light"], cb["blue"]),
    ('blue',       0,     0, 255, cd["none"], cb["blue"]),
    ('navy',       0,     0, 128, cd["dark"], cb["blue"]),

    ('pink',       255, 182, 193, cd["light"], cb["red"]),
    ('red',        255,   0,   0, cd["none"], cb["red"]),
    ('maroon',     139,   0,   0, cd["dark"], cb["red"]),

    ('light green', 144, 238, 144, cd["light"], cb["green"]),
    ('green',       0,   128,   0, cd["none"], cb["green"]),
    ('dark green',  0,   100,   0, cd["dark"], cb["green"]),

    ('yellow',       255, 255,   0, cd["none"], cb["yellow"]),
    ('dark yellow',  204, 204,   0, cd["dark"], cb["yellow"]),

    ('lavender',    230, 230, 250, cd["light"], cb["purple"]),
    ('purple',      128,   0, 128, cd["none"], cb["purple"]),
    ('indigo',      75,    0, 130, cd["dark"], cb["purple"]),

    ('peach',       255, 218, 185, cd["light"], cb["orange"]),
    ('orange',      255, 165,   0, cd["none"], cb["orange"]),
    ('dark orange', 255, 140,   0, cd["dark"], cb["orange"]),

    ('tan',         210, 180, 140, cd["light"], cb["brown"]),
    ('brown',       165,  42,  42, cd["none"], cb["brown"]),
    ('dark brown',  101,  67,  33, cd["dark"], cb["brown"]),

    ('cyan',       0,   255, 255, cd["none"], cb["blue"]),
    ('lime',       96,  255,  96, cd["light"], cb["green"]),
    ('magenta',    255,   0, 255, cd["none"], cb["purple"]),

    ('silver',     192, 192,  12, cd["metallic"], cb["grey"]),
    ('gold',       187, 165,  61, cd["metallic"], cb["yellow"]),
    ('brass',      181, 166,  66, cd["metallic"], cb["brown"]),
    ('platinum',   229, 228, 226, cd["metallic"], cb["grey"]),
]
