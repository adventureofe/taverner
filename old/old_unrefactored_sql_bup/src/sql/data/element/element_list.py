from sql.generate.colour.colour_list import colour_list
from sql.generate.element.element_type.element_type_list import element_type_list

c = {color[0]: index+1 for index, color in enumerate(colour_list)}
et = {element_type: index+1 for index, element_type in enumerate(element_type_list)}

element_list = [
    ("alien", c["magenta"], et["physical"]),
    ("air", c["silver"], et["physical"]),
    ("chaos", c["orange"], et["special"]),
    ("earth", c["brown"], et["physical"]),
    ("electricity", c["yellow"], et["special"]),
    ("evil", c["black"], et["physical"]),
    ("fire", c["red"], et["special"]),
    ("holiness", c["white"], et["physical"]),
    ("ice", c["cyan"], et["special"]),
    ("metal", c["dark grey"], et["physical"]),
    ("mutation", c["maroon"], et["physical"]),
    ("normal", c["grey"], et["physical"]),
    ("plant", c["green"], et["special"]),
    ("poison", c["purple"], et["physical"]),
    ("radiation", c["lime"], et["special"]),
    ("undead", c["dark green"], et["physical"]),
    ("water", c["blue"], et["special"]),
    ("fungus", c["gold"], et["physical"])
]
