from src.sql.data.colour.colour_darkness.colour_darkness_list import colour_darkness_list

cd = {colour_darkness: index+1 for index, colour_darkness in enumerate(colour_darkness_list)}

colour_list =  [
    # name          r    g    b
    ('black',      0,     0,   0, cd["black"]),
    ('dark grey',  64,   64,   64, cd["dark"]),
    ('grey',       128, 128, 128, cd["none"]),
    ('light grey', 192,  192, 192, cd["light"]),
    ('white',      255, 255, 255, cd["white"]),

    ('light blue', 173, 216, 230, cd["light"]),
    ('blue',       0,     0, 255, cd["none"]),
    ('navy',       0,     0, 128, cd["dark"]),

    ('pink',       255, 182, 193, cd["light"]),
    ('red',        255,   0,   0, cd["none"]),
    ('maroon',     139,   0,   0, cd["dark"]),

    ('light green', 144, 238, 144, cd["light"]),
    ('green',       0,   128,   0, cd["none"]),
    ('dark green',  0,   100,   0, cd["dark"]),

    ('yellow',       255, 255,   0, cd["none"]),
    ('dark yellow',  204, 204,   0, cd["dark"]),

    ('lavender',    230, 230, 250, cd["light"]),
    ('purple',      128,   0, 128, cd["none"]),
    ('indigo',      75,    0, 130, cd["dark"]),

    ('peach',       255, 218, 185, cd["light"]),
    ('orange',      255, 165,   0, cd["none"]),
    ('dark orange', 255, 140,   0, cd["dark"]),
    
    ('tan',         210, 180, 140, cd["light"]),
    ('brown',       165,  42,  42, cd["none"]),
    ('dark brown',  101,  67,  33, cd["dark"]),

    ('cyan',       0,   255, 255, cd["none"]),
    ('lime',       96,  255,  96, cd["light"]),
    ('magenta',    255,   0, 255, cd["none"]),

    ('none',       255, 255, 255, cd["transparent"]),

    ('silver',     192, 192,  12, cd["metallic"]),
    ('gold',       187, 165,  61, cd["metallic"]),
    ('brass',      181, 166,  66, cd["metallic"]),
    ('platinum',   229, 228, 226, cd["metallic"]),
]

