from src.sql.colour.colour_list import colour_list
from src.sql.move_type.move_type_list import move_type_list

c = {colour[0]: index+1 for index, colour in enumerate(colour_list)}
mt = {move_type[0]: index+1 for index, move_type in enumerate(move_type_list)}

element_list = [
    # name          #colour          #move_type
    ("typeless",    c["colourless"], mt["typeless"]),
    ("alien",       c["magenta"],    mt["physical"]),
    ("air",         c["silver"],     mt["physical"]),
    ("chaos",       c["orange"],     mt["special"]),
    ("earth",       c["brown"],      mt["physical"]),
    ("electricity", c["yellow"],     mt["special"]),
    ("evil",        c["black"],      mt["physical"]),
    ("fire",        c["red"],        mt["special"]),
    ("holiness",    c["white"],      mt["physical"]),
    ("ice",         c["cyan"],       mt["special"]),
    ("metal",       c["dark grey"],  mt["physical"]),
    ("mutation",    c["maroon"],     mt["physical"]),
    ("normal",      c["grey"],       mt["physical"]),
    ("plant",       c["green"],      mt["special"]),
    ("poison",      c["purple"],     mt["physical"]),
    ("radiation",   c["lime"],       mt["special"]),
    ("undead",      c["dark green"], mt["physical"]),
    ("water",       c["blue"],       mt["special"]),
    ("fungus",      c["gold"],       mt["physical"]),
]
