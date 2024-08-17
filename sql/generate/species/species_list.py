from sql.generate.colour.colour_list import colour_list
c = {color[0]: index+1 for index, color in enumerate(colour_list)}

move_list = [
    ("aardvark", c["brown"]),
    ("tiger", c["orange"]),
    ("zebra", c["white"]),
    ("dog", c["brown"]),
    ("cat", c["orange"])
]
