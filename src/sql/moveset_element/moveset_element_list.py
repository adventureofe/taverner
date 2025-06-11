from src.sql.chance.chance_list import chance_list
from src.sql.element.element_list import element_list
from src.sql.move.move_list import move_list

c = {chance[0]: index+1 for index, chance in enumerate(chance_list)}
e = {element[0]: index+1 for index, element in enumerate(element_list)}
m = {move[0]: index+1 for index, move in enumerate(move_list)}

# (text-scale-decrease 1)

moveset_element_list = [
    #element   move                lvl lineage pos chance
    (e["typeless"], m["thud"],       0,     1,  1, c["guaranteed"]),

    (e["alien"], m["probe"],         0,     2,  1, c["guaranteed"]),
    (e["alien"], m["death ray"],     0,     2,  2, c["guaranteed"]),
    (e["alien"], m["plasma fist"],   0,     1,  1, c["guaranteed"]),
    (e["alien"], m["plasma ball"],   0,     1,  1, c["guaranteed"]),


    (e["air"], m["wing attack"],     0,     3,  1, c["guaranteed"]),
    (e["air"], m["talon slash"],     0,     3,  1, c["guaranteed"]),
    (e["air"], m["peck"],     0,     3,  1, c["guaranteed"]),
    (e["air"], m["drilling peck"],     0,     3,  1, c["guaranteed"]),
    (e["air"], m["gust"],     0,     3,  1, c["guaranteed"]),


    (e["chaos"], m["flabberghast"],  0,     4,  1, c["guaranteed"]),

    #(e["earth"], m["bulldoze"],  0, ,       1, c["guaranteed"]),
    #(e["electricity"], m["electroball"],  0, ,       1, c["guaranteed"]),
    #(e["evil"], m[""],  0, ,       1, c["guaranteed"]),
    #(e["fire"], m[""],  0, ,       1, c["guaranteed"]),
    #(e["holiness"], m[""],  0, ,       1, c["guaranteed"]),
    #(e["ice"], m[""],  0, ,       1, c["guaranteed"]),
    #(e["metal"], m[""],  0, ,       1, c["guaranteed"]),
    #(e["mutation"], m[""],  0, ,       1, c["guaranteed"]),
    #(e["normal"], m[""],  0, ,       1, c["guaranteed"]),
    #(e[""], m[""],  0, ,       1, c["guaranteed"]),
    #(e[""], m[""],  0, ,       1, c["guaranteed"]),
    #(e[""], m[""],  0, ,       1, c["guaranteed"]),
    #(e[""], m[""],  0, ,       1, c["guaranteed"]),

]
