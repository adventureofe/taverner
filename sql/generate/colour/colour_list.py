from sql.generate.colour.colour_darkness.colour_darkness_list import colour_darkness_list


cd = {colour_darkness: index+1 for index, colour_darkness in enumerate(colour_darkness_list)}

colour_list =  [
    # name          r    g    b
    ('magenta',    255,   0, 255, cd["none"]),
    ('silver',     192, 192,  12, cd["metallic"]), 
    ('orange',     255, 128,   0, cd["none"]),
    ('brown',      128,  64,   0, cd["none"]),
    ('yellow',     255, 255,   0, cd["none"]),
    ('black',      0,     0,   0, cd["black"]),
    ('red',        255,   0,   0, cd["none"]),
    ('white',      255, 255, 255, cd["white"]),
    ('cyan',       0,   255, 255, cd["none"]),
    ('dark grey',  64,   64,   4, cd["dark"]),
    ('maroon',     128,   0,   0, cd["none"]),
    ('grey',       128, 128, 128, cd["none"]),
    ('green',      0,   255,   0, cd["none"]),
    ('purple',     128,   0, 128, cd["none"]),
    ('lime',       96,  255,  96, cd["light"]),
    ('dark green', 0,    96,   0, cd["dark"]),
    ('blue',       0,     0, 255, cd["none"]),
    ('gold',       187, 165,  61, cd["metallic"]),
    ('pink',       255, 192, 203, cd["light"]),
    ('none',       255, 255, 255, cd["transparent"]),
]
