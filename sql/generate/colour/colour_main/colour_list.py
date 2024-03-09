from collections import namedtuple

Color = namedtuple('Color', ['name', 'r', 'g', 'b'])

colour_list =  [
    # name          r    g    b
    ('pink',       255, 192, 203),
    ('magenta',    255,   0, 255),
    ('silver',     192, 192,  12), 
    ('orange',     255, 128,   0),
    ('brown',      128,  64,   0),
    ('yellow',     255, 255,   0),
    ('black',      0,     0,   0),
    ('red',        255,   0,   0),
    ('white',      255, 255, 255),
    ('cyan',       0,   255, 255),
    ('dark grey',  64,   64,   4),
    ('maroon',     128,   0,   0),
    ('grey',       128, 128, 128),
    ('green',      0,   255,   0),
    ('purple',     128,   0, 128),
    ('lime',       96,  255,  96),
    ('dark green', 0,    96,   0),
    ('blue',       0,     0, 255),
    ('gold',       187, 165,  61)
]

# Create a list of Color objects
color_objects = [Color(*color_data) for color_data in colour_list]

# Example usage
for color in color_objects:
    print(f"{color.name}: ({color.r}, {color.g}, {color.b})")
